from django.db import models

# Create your models here.

class Coordenador(models.Model):
    loginCoordenador = models.CharField(max_length=15)
    matCoordenador = models.IntegerField,
    nomeCoordenador= models.CharField(max_length=50)
    emailCoordenador = models.CharField(max_length=40)
    cdProj = models.IntegerField,

    def __str__(self):
        return self.nomeCoordenador
