from django.urls import path
from . import views

urlpatterns = [
    # path('class/<int:id>/', views.class_detail),
    # path('classes/', views.class_list),
    # path('', views.index),
    path('add/', views.add_student),
    path('show/', views.get_all_members)
]