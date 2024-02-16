from django.db import models
from django.contrib.auth.models import AbstractUser

# Modèle personnalisé pour un utilisateur
class CustomUser(AbstractUser):
    mail = models.EmailField(unique=True)
    id_tuteur = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class Agenda(models.Model):
    preferences = models.TextField()

class Tutorat(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)

class Cours(models.Model):
    id_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    mail = models.EmailField()
    id_tuteur = models.ForeignKey(CustomUser, related_name='cours_tuteur', on_delete=models.CASCADE)

class PriseDeNote(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

class Quiz(models.Model):
    note = models.DecimalField(max_digits=5, decimal_places=2)

class Corrige(models.Model):
    id_quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    note = models.DecimalField(max_digits=5, decimal_places=2)
