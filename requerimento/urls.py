from django.urls import path
from django.contrib import admin

from requerimento import views

app_name = 'requerimento'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ViewIndex.as_view(), name='index'),
    path('dados/', views.ViewDados.as_view(), name='dados'),
    path('enviado/', views.ViewEnviado.as_view(), name='enviado'),
]