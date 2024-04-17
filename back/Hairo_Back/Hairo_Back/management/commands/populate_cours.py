from django.core.management.base import BaseCommand
from Hairo_Back.models import Cours, FichierPDF  # Assurez-vous que le nom de l'application est correct
import os
from django.core.files import File

class Command(BaseCommand):
    help = 'Populate the database with course data'

    def populate_database(self):  # Ajout de 'self' comme premier argument
        root_dir = 'Hairo_Back/management/commands/PACES'  # Chemin absolu vers votre dossier PACES
        print('Populating database with course data...')
        print('Root directory:', root_dir)
        for root, dirs, files in os.walk(root_dir):
            print('files:', files)
            for file in files:
                if file.endswith('.pdf'):
                    cours_name = os.path.basename(root)
                    cours, created = Cours.objects.get_or_create(nom=cours_name)
                    pdf_path = os.path.join(root, file)
                    with open(pdf_path, 'rb') as pdf_file:
                        fichier_pdf = FichierPDF(cours=cours, nom=file)
                        fichier_pdf.fichier.save(file, File(pdf_file), save=True)
                        print(fichier_pdf.nom, 'ajouté à', cours.nom)

    def handle(self, *args, **options):
        self.populate_database()  # Utilisation de 'self' pour appeler la méthode de la classe