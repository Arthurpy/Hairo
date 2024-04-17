from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']  # example field that is required on user creation

    objects = UserManager()

    def __str__(self):
        return self.email


class Cours(models.Model):
    nom = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images_cours/')

    def __str__(self):
        return self.nom

class FichierPDF(models.Model):
    cours = models.ForeignKey(Cours, related_name='fichiers', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    fichier = models.FileField(upload_to='fichiers_cours/')
    image = models.ImageField(upload_to='images_fichiers/')

    def __str__(self):
        return self.nom