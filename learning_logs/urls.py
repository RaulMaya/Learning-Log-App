'''Defining URL patterns for the learning_logs'''

from django.urls import path
from . import views

app_name = 'learning_logs'
url_patterns = [
    # Home Page
    path('', views.index, name = 'index'),
]