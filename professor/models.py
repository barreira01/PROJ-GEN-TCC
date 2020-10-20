from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

class Professor(models.Model):
    loginProf = models.CharField(max_length=15)
    nomeProf = models.CharField(max_length=50)
    emailProf = models.CharField(max_length=40)
    celProf = models.CharField(max_length=11)

    def __str__(self):
        return self.nomeProf
