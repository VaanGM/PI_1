"""PI_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Importar include para poder referênciar outros URLconfs
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #Sempre usar include para referênciar URLs de apps
    path('requerimento/', include('requerimento.urls')), #Isso diz que o site busca
    path('admin/', admin.site.urls),
]