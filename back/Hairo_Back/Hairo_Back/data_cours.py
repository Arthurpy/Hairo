import os
from django.core.files import File
from Hairo_Back.models import Cours, FichierPDF

def populate_database():
    root_dir = '../../src/assets/PACES'  # Chemin absolu vers votre dossier PACES
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.pdf'):
                # Extraction du nom du cours basé sur le dossier
                cours_name = os.path.basename(root)
                # Création ou récupération de l'objet Cours
                cours, created = Cours.objects.get_or_create(nom=cours_name)
                # Chemin vers le fichier PDF
                pdf_path = os.path.join(root, file)
                # Chemin vers l'image, supposant qu'elle a la même base de nom que le PDF
                image_filename = f"{os.path.splitext(file)[0]}.jpg"  # Changez '.jpg' en fonction du format de vos images
                image_path = os.path.join(root, image_filename)
                # Ajout du fichier PDF
                with open(pdf_path, 'rb') as pdf_file:
                    fichier_pdf = FichierPDF(cours=cours, nom=file)
                    fichier_pdf.fichier.save(file, File(pdf_file), save=True)
                # Ajout de l'image au modèle Cours, s'il existe une image correspondante
                if os.path.exists(image_path):
                    with open(image_path, 'rb') as image_file:
                        cours.image.save(image_filename, File(image_file), save=True)