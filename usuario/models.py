from django.contrib.auth.models import AbstractUser
from django.db import models
from plano.models import Plano


class Usuario(AbstractUser):
    picture = models.ImageField(upload_to="usuarios/", null=True, blank=True)
    plano = models.ForeignKey(
        Plano,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )

    def save(self, *args, **kwargs):
        if self.plano is None:
            self.plano = Plano.objects.filter(nome="Gratuito").first()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
