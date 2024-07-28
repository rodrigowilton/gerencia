from django.urls import path
from .views import (candidato_list, candidato_create, pesquisa_list, pesquisa_create,
                    pesquisa_success, pesquisa_view, pesquisa_list)
from . import views
from .views import sexo_pie_chart



urlpatterns = [
    path('candidatos/', candidato_list, name='candidato_list'),
    path('candidatos/adicionar/', candidato_create, name='candidato_create'),
    path('pesquisas/adicionar/', pesquisa_create, name='pesquisa_create'),
    path('success/', views.pesquisa_success, name='pesquisa_success'),
    path('pesquisas/relatorio/', pesquisa_list, name='pesquisa_list'),
    path('grafico-sexo/', sexo_pie_chart, name='sexo_pie_chart'),

]