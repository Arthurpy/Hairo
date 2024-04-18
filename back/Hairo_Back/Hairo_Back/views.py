# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialToken
from rest_framework import generics
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from .models import Cours, FichierPDF
from .serializers import CoursSerializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cours
from .serializers import CoursSerializer
from functools import wraps
from flask import request
import requests


def landing_page(request):
    return render(request, 'landing.html')


@csrf_exempt
def course_details_by_name(request):
    try:
        data = json.loads(request.body.decode('utf-8'))  # ensure decoding from bytes if needed
        course_name = data.get('courseName')
        if not course_name:
            return JsonResponse({'error': 'No course name provided'}, status=400)

        cours = Cours.objects.get(nom__iexact=course_name)  # Case insensitive search
        pdfs = cours.fichiers.all()
        pdf_data = [{
            'id': pdf.id,
            'nom': pdf.nom,
            'url': request.build_absolute_uri(pdf.fichier.url)  # Accessing the file url correctly
        } for pdf in pdfs]
        return JsonResponse({
            'nom': cours.nom,
            'pdfs': pdf_data
        }, safe=True)
    except Cours.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        # Log the exception to help with debugging
        print(f"Error in course_details_by_name: {str(e)}")
        return JsonResponse({'error': 'Server error'}, status=500)

@csrf_exempt
def ressources_pages(request):
    if request.method == 'POST':
        # Récupérer tous les cours de la base de données
        cours_list = Cours.objects.all()
        # Transformer les données en liste de dictionnaires
        cours_data = [{'id': cours.id, 'nom': cours.nom} for cours in cours_list]
        # Retourner les données en JSON
        return JsonResponse(cours_data, safe=False)
    else:
        # Si la méthode n'est pas POST, vous pouvez choisir de renvoyer une réponse appropriée
        return JsonResponse({'error': 'Invalid method'}, status=405)

@csrf_exempt
def login_view(request):
    # Add logging
    data = json.loads(request.body)
    print("Data received:", data)

    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, 'your_secret_key', algorithm='HS256')

        return JsonResponse({'token': token})
    else:
        return JsonResponse({'error': 'Invalid Credentials'}, status=400)
    
def protected_view(request):
    if request.user is not None:
        return JsonResponse({'message': 'Welcome!'})
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)

# @csrf_exempt
# def login_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         email = data.get('email')
#         password = data.get('password')
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)

#             # Générer ou récupérer le jeton JWT
#             token_payload = {
#                 'id': user.id,
#                 'exp': datetime.utcnow() + timedelta(days=2)
#             }
#             token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
#             return JsonResponse({'token': token, 'message': 'Logged in successfully'})
#         else:
#             return JsonResponse({'error': 'Invalid email or password'}, status=400)
#     return render(request, 'login.html')

@csrf_exempt
def signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = User.objects.create_user(email=email, password=password)
        login(request, user)

        # Générer un jeton JWT
        token_payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(days=2)  # Expiration dans 2 jours
        }
        token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')

        # Stocker le jeton si nécessaire ou le renvoyer directement
        return JsonResponse({'token': token, 'message': 'User created successfully'})

    return render(request, 'signup.html')

@login_required
def agenda(request):
    return JsonResponse({'message': 'Cette fonction est en cours de développement.'}, status=200)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'message': 'Token is missing!'}, status=403)

        try:
            data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            current_user = User.objects.get(id=data['id'])
        except:
            return JsonResponse({'message': 'Token is invalid!'}, status=403)

        return f(current_user, *args, **kwargs)

    return decorated


def send_token_response(user):
    token = generate_token_for(user)  # Générer le jeton d'authentification ici
    return JsonResponse({'token': token, 'message': 'Logged in successfully'})

def get_user_info(access_token):
    # Utilisez le jeton d'accès pour récupérer les informations de l'utilisateur
    # à partir du service d'authentification de Microsoft
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get('https://graph.microsoft.com/v1.0/me', headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def microsoft_callback(request):
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'error': 'No code provided'}, status=400)
    token_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
    token_params = {
        'client_id': 'f14c32e8-369d-4474-b06e-7d506073f86e',
        'scope': 'User.Read',
        'code': code,
        'redirect_uri': 'http://localhost:8000/auth/microsoft/callback/',
        'grant_type': 'authorization_code',
        'client_secret': '67d92e47-2a8f-43db-bf45-9aea4c240436'
    }
    response = requests.post(token_url, data=token_params)

    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        user_info = get_user_info(access_token)
        if user_info:
            # Créer un utilisateur ou le récupérer s'il existe déjà
            user, created = User.objects.get_or_create(email=user_info['mail'])
            if created:
                send_welcome_email(user)
                user.profile_picture = 'default.jpg'
                user.save()
            return send_token_response(user)
        else:
            return JsonResponse({'error': 'Failed to get user info'}, status=500)
    else:
        return JsonResponse({'error': 'Failed to get access token'}, status=500)


def microsoft_login(request):
    auth_url = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
    client_id = 'f14c32e8-369d-4474-b06e-7d506073f86e'
    redirect_uri = 'http://localhost:8000/auth/microsoft/callback/'
    scope = 'User.Read'
    response_type = 'token'
    return redirect(f'{auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}')

def send_welcome_email(user):
    # Définissez le sujet, le message, l'expéditeur et le destinataire de l'email
    subject = 'Bienvenue sur notre site !'
    message = 'Nous sommes ravis de vous avoir parmi nous.'
    from_email = 'votre@adresse.email'
    to_email = [user.email]

    # Envoyez l'email
    send_mail(subject, message, from_email, to_email)