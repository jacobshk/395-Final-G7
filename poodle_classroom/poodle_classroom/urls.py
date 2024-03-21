"""
URL configuration for poodle_classroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('SignUp', views.index),
    path('SignIn', views.index),
    #path('api/SignUp', views.signup_view),
    path('Title', views.index),
    path('home/student', views.index),
    # path('home/student/Chart', views.index),
    # path('home/student/Deposits', views.index),
    # path('home/student/listItems', views.index),
    # path('home/student/Orders', views.index),
    #path('home/student/SAssignment', views.index),
    # path('home/student/SCalendar', views.index),
    # path('home/student/SClass', views.index),
    # path('home/student/SClassOverviewNavBar', views.index),
    # path('home/student/SGradebook', views.index),
    # path('home/student/SPeople', views.index),
    path('home/teacher', views.index),
    # path('home/student/Deposits', views.index),
    # path('home/student/listItems', views.index),
    # path('home/student/Orders', views.index),
    # path('home/student/TAssignment', views.index),
    # path('home/student/TCalendar', views.index),
    # path('home/student/TClass', views.index),
    # path('home/student/TClassOverviewNavBar', views.index),
    # path('home/student/TGradebook', views.index),
    # path('home/student/TPeople', views.index),
    path('classroom/', include('classroom.urls')),
]