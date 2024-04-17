# Generated by Django 3.2.8 on 2024-04-17 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hairo_Back', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images_cours/')),
            ],
        ),
        migrations.CreateModel(
            name='FichierPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('fichier', models.FileField(upload_to='fichiers_cours/')),
                ('cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fichiers', to='Hairo_Back.cours')),
            ],
        ),
    ]