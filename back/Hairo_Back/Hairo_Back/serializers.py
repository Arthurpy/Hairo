from rest_framework import serializers
from .models import Cours, FichierPDF

class FichierPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = FichierPDF
        fields = ('id', 'nom', 'fichier', 'image')

class CoursSerializer(serializers.ModelSerializer):
    fichiers = FichierPDFSerializer(many=True, read_only=True)

    class Meta:
        model = Cours
        fields = ('id', 'nom', 'image', 'fichiers')