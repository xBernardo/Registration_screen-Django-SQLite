from django.db import models

# Create your models here.
class Veiculo(models.Model):
    id_veiculos = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    marca = models.TextField(max_length=255)
    valor = models.IntegerField()