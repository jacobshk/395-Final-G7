from django.db import models
from db_connection import db

# Create your models here.

class Classroom(models.Model):
    teacher_name = models.CharField(max_length=200)

class_collection = db['Classes']