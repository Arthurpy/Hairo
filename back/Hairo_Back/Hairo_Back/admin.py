from django.contrib import admin
from .models import CustomUser, Agenda, Tutorat, Cours, PriseDeNote, Quiz, Corrige

admin.site.register(CustomUser)
admin.site.register(Agenda)
admin.site.register(Tutorat)
admin.site.register(Cours)
admin.site.register(PriseDeNote)
admin.site.register(Quiz)
admin.site.register(Corrige)
