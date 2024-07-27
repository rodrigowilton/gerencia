from django.urls import path
from .views import candidato_list, candidato_create, pesquisa_list, pesquisa_create, pesquisa_success
from . import views
urlpatterns = [
    path('candidatos/', candidato_list, name='candidato_list'),
    path('candidatos/adicionar/', candidato_create, name='candidato_create'),
    path('pesquisas/', pesquisa_list, name='pesquisa_list'),
    path('pesquisas/adicionar/', pesquisa_create, name='pesquisa_create'),
    path('success/', views.pesquisa_success, name='pesquisa_success'),

]