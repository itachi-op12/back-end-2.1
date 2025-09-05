from django.db import models

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    periodo = models.DecimalField(max_digits=5, decimal_places=0)  # ex: 30 dias, 12 meses
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - {self.valor}"
