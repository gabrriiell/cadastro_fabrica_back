
from django.contrib import admin

#para incluir todas as rotas do projeto irei utilizar o routs para não precisar utilizar rotas separadas


'''
routers = routers.DefaultRouter
routers.register(r'cadastro',cadastroviewsets.cadastroview,basename='cadastro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include.urls)
]
'''
from django.urls import path, include
from rest_framework import routers
from cadastro_app.api.viewersets import cadastroview

routers = routers.DefaultRouter()
routers.register(r'cadastro',cadastroview, basename='cadastro')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
]

