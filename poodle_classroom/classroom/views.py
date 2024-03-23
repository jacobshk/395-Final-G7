from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Classroom, class_collection
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("App is running")

def add_student(request):
    records = {
        "first_name":"Jane",
        "last_name":"Doe"
    }
    class_collection.insert_one(records)
    return HttpResponse("New person is added")

def get_all_members(request):
    members = class_collection.find()
    return HttpResponse(members)