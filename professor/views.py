from django.shortcuts import render, get_object_or_404
from .models import Professor
from django.http import HttpResponse


# Create your views here.

def Professor_page(request):
    homepageprofessor = Professor.nomeProfessor
    projetos = Professor.objects.all()
    return render(request, 'homepageprofessor/professorpainel.html', {'professor':homepageprofessor, 'projetos':projetos})

def Professor_orientations(request):
    # return HttpResponse(slug)
    dados = Professor.objects.all()
    return render(request, 'homepageprofessor/projorientacao.html', {'professor':dados})