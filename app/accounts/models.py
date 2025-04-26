from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('en', 'English'),
        ('zh', '中文'),
        ('fr', 'Français'),
    ]

    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='ru')
    region = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return self.username