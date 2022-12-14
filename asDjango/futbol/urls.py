"""asDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

app_name="futbol"

urlpatterns = [
    path('', views.temporadas, name='temporadas'),
    #path('ultimaTemporada/', views.ultimaTemporada, name='ultimaTemporada'),
    path('equipos/', views.equipos, name='equipos'),
    path('equipos/equipo/<int:id>', views.equipoDetalle, name='equipo'),
    #path('estadiosMayores/', views.estadiosMayores, name='estadiosMayores'),
    path('cargar/', views.cargar, name='cargar'),
]