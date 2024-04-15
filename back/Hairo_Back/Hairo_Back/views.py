# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from Hairo_Back.utils import get_user_oauth_token_from_django
from .forms import LoginForm
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta


def landing_page(request):
    return render(request, 'landing.html')

@method_decorator(csrf_exempt, name='dispatch')
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'})
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=400)
    return render(request, 'login.html')

@method_decorator(csrf_exempt, name='dispatch')
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = User.objects.create_user(email=email, password=password)
        login(request, user)
        return JsonResponse({'message': 'User created successfully'})
    return render(request, 'signup.html')

def agenda(request):
     # Récupérer le jeton d'accès OAuth de l'utilisateur depuis Django
    user_oauth_token = get_user_oauth_token_from_django()  # Fonction hypothétique à remplacer par ton propre code

    # Créer un objet Credentials à partir du jeton d'accès OAuth
    credentials = Credentials(token=user_oauth_token)

    # Créer un client Google Calendar à partir des credentials
    calendar_service = build('calendar', 'v3', credentials=credentials)

    # Récupérer la date de début et de fin de la semaine actuelle
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    # Récupérer les événements de la semaine actuelle
    events = calendar_service.events().list(
        calendarId='primary',
        timeMin=start_of_week.isoformat() + 'Z',
        timeMax=end_of_week.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    # Passer les événements au template
    context = {
        'events': events.get('items', [])
    }

    return render(request, 'agenda.html', context)