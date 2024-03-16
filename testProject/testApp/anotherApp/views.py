from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from .models import User, Class
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def signin_view(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse({"message": "Signed in successfully", "status": "success"})
    else:
        return HttpResponse({"message": "Invalid email or password", "status": "error"})

@api_view(['POST'])
def signup_view(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    email = request.POST['email']
    confirm_password = request.POST['confirm_password']
    if password != confirm_password or len(password) < 8:
        return HttpResponse("Invalid password")
    if User.objects.filter(email=email).exists():
        return HttpResponse("User already exists")
    User.objects.create_user(email, password, first_name=first_name, last_name=last_name)
    return HttpResponse("User created successfully")

# def get_user_classes(request):
#     user = User.objects.get(email=request.POST['email'])
#     classes = user.classes_joined.all()
#     return HttpResponse(classes)

# def create_class(request):
#     name = request.POST['classname']
#     teacher = User.objects.get(email=request.POST['email'])
#     if Class.objects.filter(name=name).exists():
#         return HttpResponse("Class already exists")
#     Class.objects.create(name=name, teacher=teacher)
#     return HttpResponse("Class created successfully")

# def join_class(request):
#     class_id = request.POST['class_id']
#     user = User.objects.get(email=request.POST['email'])
#     class_ = Class.objects.get(id=class_id)
#     if user in class_.students.all():
#         return HttpResponse("Already enrolled in class")
#     class_.students.add(user)
#     return HttpResponse("Enrolled in class successfully")