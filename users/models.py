from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('apprenant', 'Apprenant'),
        ('formateur', 'Formateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    image = models.ImageField(upload_to='images/')
    date_joined = models.DateTimeField(auto_now_add=True)
    

