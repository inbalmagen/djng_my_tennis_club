from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('trainers/', views.trainers, name='trainers'),
    path('courts/', views.courts, name='courts'),
    path('courts/single_court/<int:id>', views.single_court, name='single_court'),
    path('occupy_court/<int:court_id>/', views.occupy_court, name='occupy_court'),  # URL to occupy a court
    path('free_court/<int:court_id>/', views.free_court, name='free_court'),  # URL to free a court
]
