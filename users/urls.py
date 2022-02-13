"""Defines URL patterns for the users"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Include the default authentication urls
    path('', include('django.contrib.auth.urls')),
    # Registration of new users
    path('register/', views.register, name="register"),
]