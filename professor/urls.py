from django.urls import path
from. import views


app_name = 'professor'

urlpatterns = [
    path('', views.Professor_page, name="list"),
    path('<slug:slug>/', views.Prodessor_detail, name="detail"),

]