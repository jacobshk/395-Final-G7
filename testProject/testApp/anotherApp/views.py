from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import User, Class

# Create your views here.
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Logged in successfully")
    else:
        return HttpResponse("Invalid username or password")
    
    
def signup_view(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    confirm_password = request.POST['confirm_password']
    if password != confirm_password or len(password) < 8:
        return HttpResponse("Invalid password")
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return HttpResponse("User already exists")
    User.objects.create_user(username, email, password)
    return HttpResponse("User created successfully")

def get_user_classes(request):
    user = User.objects.get(email=request.POST['email'])
    classes = user.classes_joined.all()
    return HttpResponse(classes)

def create_class(request):
    name = request.POST['classname']
    teacher = User.objects.get(email=request.POST['email'])
    if Class.objects.filter(name=name).exists():
        return HttpResponse("Class already exists")
    Class.objects.create(name=name, teacher=teacher)
    return HttpResponse("Class created successfully")

def join_class(request):
    class_id = request.POST['class_id']
    user = User.objects.get(email=request.POST['email'])
    class_ = Class.objects.get(id=class_id)
    if user in class_.students.all():
        return HttpResponse("Already enrolled in class")
    class_.students.add(user)
    return HttpResponse("Enrolled in class successfully")