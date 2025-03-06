from rest_framework import routers
from .views import ColaboradoresView

routerColaboradores = routers.DefaultRouter()
routerColaboradores.register(r'', ColaboradoresView)
