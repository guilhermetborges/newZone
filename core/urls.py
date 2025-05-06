from django.urls import path, include
from .views import IndexViews , UserRegisterView ,PaisView , ListaPaisView , CidadesView
from django.contrib.auth import views as auth_views 
from django.views.generic import TemplateView




urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='desloga'), name='logout'),
    path('desloga/', TemplateView.as_view(template_name='desloga.html'), name='desloga'),
    path('paises/', ListaPaisView.as_view(), name='listar_paises'),
    path('pais/<slug:slug>/', PaisView.as_view(), name='pais_detalhe'),
    path('cidade/<slug:slug>/', CidadesView.as_view(), name='cidades'),

]