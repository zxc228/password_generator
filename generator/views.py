from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def about(request):    
    return render(request, 'generator/about.html')


def password(request):
    thepassword = 'testing'
    characters = list(string.ascii_lowercase)
    

    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get('special'):
        characters.extend(string.punctuation)

    if request.GET.get('digits'):
        characters.extend(list(string.digits))

    length = int(request.GET.get('length', 12))

    thepassword = ''.join(random.choice(characters) for i in range(length))
    return render(request, 'generator/password.html', {'password': thepassword})


