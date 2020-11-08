from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def login(request): #add autenticacao de prof e coord depois
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('aluno:list') 
        else:
            return render(request, 'accounts/login.html', {'error': 'Usuário ou senha incorretos'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('aluno:list')

""" def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect('aluno:list')
    else:
        form = UserCreationForm
    return render(request, 'accounts/signup.html', {'form': form}) """

""" def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            return redirect('aluno:list')

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form}) """


""" def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('aluno:list')
 """

