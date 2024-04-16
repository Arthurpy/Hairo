from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.shortcuts import redirect
from django.contrib.auth import login

@method_decorator(csrf_exempt, name='dispatch')
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        # C'est ici que l'utilisateur est créé et sauvegardé dans la base de données.
        user = form.save()
        # Connectez l'utilisateur directement après l'inscription.
        login(self.request, user)
        # Redirection vers le tableau de bord après inscription.
        return redirect('dashboard')

def dashboard_view(request):
    return render(request, "dashboard.html")
