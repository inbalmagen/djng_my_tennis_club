from django.urls import path
from . import views

urlpatterns = [
    path('courts/', views.courts, name='courts'),
    path('reserve/<int:id>', views.reserve, name='reserve'),
    path('courts/single_court/<int:id>', views.single_court, name='single_court'),
    path('occupy_court/<int:court_id>/', views.occupy_court, name='occupy_court'),  # URL to occupy a court
    path('free_court/<int:court_id>/', views.free_court, name='free_court'),  # URL to free a court

    path('court-order/', views.court_order_list, name='court_order_list'),  # Show court orders with members
    path('reserve/', views.reserve_court, name='reserve_court'),  # Form to reserve a court with two members
]
