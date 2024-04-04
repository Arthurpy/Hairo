from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

from rest_framework import generics
from .serializers import UserSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UserCreate(generics.CreateAPIView):
    serializer_class = UserSerializer
