from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('trainers/', views.trainers, name='trainers'),
    path('courts/', views.courts, name='courts'),
]
