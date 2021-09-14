from django.shortcuts import render
from django.http import HttpResponse

#Pra chamar uma view, é preciso mapea-la para uma URL, no arquivo urls.py, neste mesmo app.
def index(request):
    return HttpResponse("Index View")