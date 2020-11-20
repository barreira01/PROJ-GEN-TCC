from django.db import models

# Create your models here.

class Professor(models.Model):
    loginProfessor = models.CharField(max_length=15)
    matProfessor = models.IntegerField,
    nomeProfessor = models.CharField(max_length=50)
    emailProfessor = models.CharField(max_length=40)
    cdProj = models.IntegerField

    def __str__(self):
        return self.nomeProfessor
