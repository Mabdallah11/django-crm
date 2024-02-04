from django.contrib import admin
from django.contrib.auth import views
from django.urls import path


from userprofile.views import signup, myaccount 

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('log-out/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/myaccount/', myaccount,name='myaccount'),
]
