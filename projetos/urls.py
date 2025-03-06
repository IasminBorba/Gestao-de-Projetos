from rest_framework import routers
from .views import *

routerProjetos = routers.DefaultRouter()
routerProjetos.register(r'areas_tecnologicas', AreasTecnologicasView)
routerProjetos.register(r'financiadores', FinanciadoresView)
routerProjetos.register(r'', ProjetosView)
