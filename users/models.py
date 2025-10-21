from django.db import models

# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser



# myapp/models.py

class CustomUser(AbstractUser):
    
    color_theme = models.CharField(max_length=50)
    # Добавьте другие кастомные поля, если необходимо
