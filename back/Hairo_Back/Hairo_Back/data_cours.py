import os
from django.core.files import File
from Hairo_Back.models import Cours, FichierPDF

def populate_database():
    root_dir = '../../src/assets/PACES'  # Chemin absolu vers votre dossier PACES
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.pdf'):
                cours_name = os.path.basename(root)
                cours, created = Cours.objects.get_or_create(nom=cours_name)
                pdf_path = os.path.join(root, file)
                with open(pdf_path, 'rb') as pdf_file:
                    fichier_pdf = FichierPDF(cours=cours, nom=file)
                    fichier_pdf.fichier.save(file, File(pdf_file), save=True)