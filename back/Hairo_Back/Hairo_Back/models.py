#!/usr/bin/env python

from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    user_refresh_token = models.CharField(max_length=100)