from django.db import models
from db_connection import db

# Create your models here.

# class Classroom(models.Model):
#     teacher_name = models.CharField(max_length=200)
    
# class Assignment(models.Model):
#     assignment_id = models.AutoField(primary_key=True)
#     file = models.FileField(upload_to='assignments/')
#     details = models.TextField()
#     student_emails_submitted = models.BinaryField(model_container=str)
#     student_emails_not_submitted = models.BinaryField(model_container=str)
#     student_grades = models.JSONField()
#     student_feedback = models.JSONField()

# class Announcement(models.Model):
#     announcement_id = models.AutoField(primary_key=True)
#     announcement_text = models.TextField()

class_collection = db['Classes']