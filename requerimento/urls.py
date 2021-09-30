from django.urls import path

from . import views

# -> É PRECISO APONTAR A URLCONF (urls.py) DO PROJETO PARA O URLCONF DO APP! <-
app_name = 'requerimento'
urlpatterns = [
    path('', views.ViewIndex.as_view(), name='index'),
    path('enviado/', views.ViewEnviado.as_view(), name='enviado'),
    path('dados/', views.ViewDados.as_view(), name='dados'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='registros'),
]