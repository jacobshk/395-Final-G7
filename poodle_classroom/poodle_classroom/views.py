from urllib import response
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from db_connection import *

# def index(request):
#     return render(request, 'index.html')

    


@api_view(['POST'])
def signup_view(request):
    if request.method == 'POST':
        username = '326'
        email = request.data.get('email')
        password = request.data.get('password')
        #confirm_password = request.data.get('confirm_password')
        confirm_password = password
        
        try:
            result = signup(db, username, email, password, confirm_password)
            return JsonResponse(result, status=201)
        except ValueError as e:
            return JsonResponse({'message': str(e)}, status=400)