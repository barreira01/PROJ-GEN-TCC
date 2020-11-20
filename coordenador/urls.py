from django.urls import path
from .views import Coordenador_page, Coordenador_detail
app_name = 'coordenador'


urlpatterns = [
    path('', Coordenador_page, name='painel'),
    path('details/', Coordenador_detail, name='projects'),
    #path('projorientacao/<int:cdP>/', Professor_orientations, name='projects'),

]