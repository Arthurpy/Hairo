from django.core.management.base import BaseCommand
from Hairo_Back.models import Cours, FichierPDF, QCM  # Assurez-vous que le nom de l'application est correct
import os
from django.core.files import File

class Command(BaseCommand):
    help = 'Populate the database with course data and associated QCMs'

    def delete_existing_data(self):
        FichierPDF.objects.all().delete()  # Supprime tous les fichiers PDF
        QCM.objects.all().delete()         # Supprime tous les QCM
        Cours.objects.all().delete()       # Supprime tous les cours

    def populate_database(self):
        root_dir = 'Hairo_Back/management/commands/PACES'  # Chemin absolu vers votre dossier PACES
        print('Populating database with course data...')
        print('Root directory:', root_dir)
        for root, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith('.pdf'):
                    cours_name = os.path.basename(root)
                    cours, created = Cours.objects.get_or_create(nom=cours_name)
                    pdf_path = os.path.join(root, file)
                    with open(pdf_path, 'rb') as pdf_file:
                        fichier_pdf = FichierPDF(cours=cours, nom=file)
                        fichier_pdf.fichier.save(file, File(pdf_file), save=True)
                        print(fichier_pdf.nom, 'added to', cours.nom)
                    
                    # Création du QCM associé
                    qcm_name = file.replace('.pdf', '.json')
                    qcm_path = os.path.join(root, qcm_name)
                    if os.path.exists(qcm_path):
                        with open(qcm_path, 'rb') as qcm_file:
                            qcm = QCM(cours=cours, contenu_json=qcm_name)
                            qcm.contenu_json.save(qcm_name, File(qcm_file), save=True)
                            print(qcm_name, 'QCM created for', cours.nom)

    def handle(self, *args, **options):
        self.delete_existing_data()
        self.populate_database()
