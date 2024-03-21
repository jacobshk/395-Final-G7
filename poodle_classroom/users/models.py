from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    enrolled_class_ids = models.JSONField(default=list)