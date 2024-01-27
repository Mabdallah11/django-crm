from django.contrib import admin
from django.contrib.auth import views
from django.urls import path


from userprofile.views import signup

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
]
