from rest_framework import serializers
from cadastro_app import models
 #CadastroSerializer será usada para serializar e desserializar objetos do modelo Cadastro
class cadastroserializer(serializers.ModelSerializer):
    class Meta:
        models = models.cadastro
        fields = '__all__'
       