from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    color_theme = models.CharField(max_length=50)

