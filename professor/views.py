from django.shortcuts import render
from .models import Professor
from django.http import HttpResponse


# Create your views here.

def Professor_page(request):
    homepageprofessor = Professor.nomeProfessor
    return render(request, 'homepageprofessor/professorpainel.html', {'professor':homepageprofessor})

def Prodessor_detail(request, slug):
    # return HttpResponse(slug)
    dados = Professor.objects.get(slug=slug)
    return render(request, 'homepageprofessor/article_detail.html', {'professor': dados})