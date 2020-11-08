from django.db import models

# Create your models here.

class Aluno(models.Model):
    loginAluno = models.CharField(max_length=15)
    matAluno = models.IntegerField,
    nomeAluno = models.CharField(max_length=50)
    emailAluno = models.CharField(max_length=40)
    cdProj = models.IntegerField

    def __str__(self):
        return self.nomeAluno
