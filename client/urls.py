from django.urls import path

from . import views 

urlpatterns =[
    path('', views.client_list, name='clients_list'),
    path('<int:pk>/', views.clients_detail, name='clients_detail'),
    path('add/', views.clients_add, name='clients_add'),
]