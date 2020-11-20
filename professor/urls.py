from django.urls import path
from .views import Professor_page, Professor_orientations
app_name = 'professor'


urlpatterns = [
    path('', Professor_page, name='painel'),
    path('projorientacao/', Professor_orientations, name='projects'),
    #path('projorientacao/<int:cdP>/', Professor_orientations, name='projects'),

]