from rest_framework import viewsets
from cadastro_app.api import serializers
from cadastro_app import models
from cadastro_app.models import cadastro  #
consultas_do_campos = cadastro.objects.all()
#classe CadastroView é uma ViewSet pega todas as ações do crud para o modelo Cadastro 
class cadastroview(viewsets):
    serializerscals = serializers.cadastroserializer
    queryset = models.cadastro.objects.all()

