from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)

class Class(models.Model):
    name = models.CharField(max_length=200, unique=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes_taught')
    students = models.ManyToManyField(User, related_name='classes_joined')