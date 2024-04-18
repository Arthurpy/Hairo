from django.core.management.base import BaseCommand
import os
from django.conf import settings
from django.core.files import File
from Hairo_Back.models import Cours, QCM

class Command(BaseCommand):
    help = 'Populate the database with QCM data from JSON files.'

    def handle(self, *args, **options):
        self.stdout.write("Starting to populate QCMs...")
        base_dir = os.path.join(settings.BASE_DIR, 'PACES')
        total_qcms_created = 0
        for root, dirs, files in os.walk(base_dir):
            for file in files:
                if file.endswith('.json'):
                    course_name = os.path.basename(root)
                    course, course_created = Cours.objects.get_or_create(nom=course_name)
                    json_path = os.path.join(root, file)
                    with open(json_path, 'rb') as json_file:
                        qcm, qcm_created = QCM.objects.get_or_create(
                            cours=course,
                            defaults={'contenu_json': File(json_file, name=file)}
                        )
                        if qcm_created:
                            total_qcms_created += 1
                            self.stdout.write(f'QCM created for course {course_name} from {file}')
        self.stdout.write(self.style.SUCCESS(f'Successfully populated QCM data. Total QCMs created: {total_qcms_created}'))
