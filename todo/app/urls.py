from django.urls import path
from app.views import *

urlpatterns = [
    path('',home,name='home'),
    path('register',register,name='register'),
    path('login',login,name='login')
]