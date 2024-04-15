from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

    REQUIRED_FIELDS = ['password', 'password2']
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True

    def __str__(self):
        return self.username

