from django.shortcuts import render, get_object_or_404
from .models import Coordenador
from django.http import HttpResponse


# Create your views here.

def Coordenador_page(request):
    homepagecoord = Coordenador.nomeCoordenador
    #projetos = Coordenador.objects.all()
    return render(request, 'coordenadorhomepage/coordenadorpainel.html', {'coordenador':homepagecoord})

def Coordenador_detail(request):
    # return HttpResponse(slug)
    dados = Coordenador.objects.all()
    return render(request, 'coordenadorhomepage/detail.html', {'coordenador':dados})