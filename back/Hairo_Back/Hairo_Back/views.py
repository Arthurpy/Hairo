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
            return JsonResponse({'message': 'Logged in successfully'})  # Retourne un message de succès
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=400)  # Retourne un message d'erreur
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