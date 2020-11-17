from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    # return HttpResponse('HomePage')
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')


def logon(request):
    # return HttpResponse('about')
    return render(request, 'login.html')

def AlunoPainel(request):
    # return HttpResponse('about')
    return render(request, 'alunopainel.html')

def ProfessorPainel(request):
    return render('request','professorpainel.html')
