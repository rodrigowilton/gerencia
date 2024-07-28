from django.urls import path
from .views import (candidato_list, candidato_create, pesquisa_list, pesquisa_create,
                    pesquisa_success, pesquisa_view, pesquisa_list)
from . import views
from .views import sexo_pie_chart,sexo_pie_chart2



urlpatterns = [
    path('candidatos/', candidato_list, name='candidato_list'),
    path('candidatos/adicionar/', candidato_create, name='candidato_create'),
    path('pesquisas/adicionar/', pesquisa_create, name='pesquisa_create'),
    path('success/', views.pesquisa_success, name='pesquisa_success'),
    path('pesquisas/relatorio/', pesquisa_list, name='pesquisa_list'),
    path('grafico-sexo/', sexo_pie_chart, name='sexo_pie_chart'),
    path('grafico-sexo2/', sexo_pie_chart2, name='sexo_pie_chart2'),
    path('grafico-idade/', views.idade_pie_chart, name='idade_pie_chart'),
    path('idade-por-bairro/', views.idade_por_bairro, name='idade_por_bairro'),
    path('grafico-rede-social/', views.rede_social_pie_chart, name='rede_social_pie_chart'),
    path('rede-social-por-bairro/', views.rede_social_por_bairro, name='rede_social_por_bairro'),

]