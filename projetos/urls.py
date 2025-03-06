from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from .views import *

routerProjetos = routers.DefaultRouter()
routerProjetos.register(r'areas_tecnologicas', AreasTecnologicasView)
routerProjetos.register(r'financiadores', FinanciadoresView)
routerProjetos.register(r'', ProjetosView)
