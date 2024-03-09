from django.db import models
import random

class cadastro(models.Model):  
    nome = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=100)  # Para testar a api só o nome é obrigatório
    senha = models.IntegerField()
    meu_id = models.PositiveIntegerField(unique=True, default=random.randint(1, 100))
    # Sempre que um novo objeto do modelo for criado, ele receberá um novo valor no ID que será único
    data_cadastro = models.DateField(auto_now_add=True)
    # Registrar a data de criação