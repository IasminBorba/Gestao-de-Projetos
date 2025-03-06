from django.contrib import admin
from django.urls import include, path

from colaboradores.urls import routerColaboradores
from projetos.urls import routerProjetos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/colaboradores/', include(routerColaboradores.urls)),
    path('api/projetos/', include(routerProjetos.urls)),
]
