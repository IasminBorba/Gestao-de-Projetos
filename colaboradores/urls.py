from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import ColaboradoresView

routerColaboradores = routers.DefaultRouter()
routerColaboradores.register(r'', ColaboradoresView)
