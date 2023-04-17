from django.db import models

# Create your models here.
class Funcionario(models.Model):
    atendimento = models.FloatField(max_length=3)
    pontualidade = models.FloatField(max_length=3)
    qualidade = models.FloatField(max_length=3)