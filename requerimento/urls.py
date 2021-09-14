from django.urls import path

from . import views

#É PRECISO APONTAR A URLCONF (urls.py) DO PROJETO PARA O URLCONF DO APP!
urlpatterns = [
    path('', views.index, name='index'),
]