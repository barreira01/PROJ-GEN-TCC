from django.conf.urls import url
from. import views

app_name ='accounts'

urlpatterns = [
    #url('signup/', views.signup_view, name="signup"),
    url('login/', views.login, name="login"),
    url('logout/', views.logout, name="logout")
]