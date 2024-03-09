from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('classes/', views.get_user_classes, name='get_user_classes'),
    path('create_class/', views.create_class, name='create_class'),
    path('join_class/', views.join_class, name='join_class'),
]