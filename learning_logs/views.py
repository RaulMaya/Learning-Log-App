import re
from django.shortcuts import render

# Create your views here.

def index(request):
    '''The home page for ll'''
    return render(request, 'learning_logs/index.html')