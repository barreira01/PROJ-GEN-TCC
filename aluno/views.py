from django.shortcuts import render
from .models import Aluno
from django.http import HttpResponse


# Create your views here.

def aluno_page(request):
    homepageAluno = Aluno.nomeAluno
    return render(request, 'homepagealuno/alunopainel.html', {'aluno':homepageAluno})

def aluno_detail(request, slug):
    # return HttpResponse(slug)
    dados = Aluno.objects.get(slug=slug)
    return render(request, 'homepagealuno/article_detail.html', {'aluno': dados})