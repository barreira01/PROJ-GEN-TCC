from django.urls import path
from. import views


app_name = 'aluno'

urlpatterns = [
    path('', views.aluno_page, name="painel"),
    path('<slug:slug>/', views.aluno_detail, name="detail"),

]