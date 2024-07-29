# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('gerencia/', views.gerencia, name='gerencia'),
    path('', views.pesquisa_view, name='pesquisa_view'),
    path('sexo_pie_chart/', views.sexo_pie_chart, name='sexo_pie_chart'),
    path('sexo_pie_chart2/', views.sexo_pie_chart2, name='sexo_pie_chart2'),
    path('candidato_list/', views.candidato_list, name='candidato_list'),
    path('idade_pie_chart/', views.idade_pie_chart, name='idade_pie_chart'),
    path('idade_por_bairro/', views.idade_por_bairro, name='idade_por_bairro'),
    path('rede_social_pie_chart/', views.rede_social_pie_chart, name='rede_social_pie_chart'),
    path('rede_social_por_bairro/', views.rede_social_por_bairro, name='rede_social_por_bairro'),
    path('vereador_pie_chart/', views.vereador_pie_chart, name='vereador_pie_chart'),
    path('vereador_por_bairro/', views.vereador_por_bairro, name='vereador_por_bairro'),
    path('pesquisa_create/', views.pesquisa_create, name='pesquisa_create'),
    path('pesquisa_success/', views.pesquisa_success, name='pesquisa_success'),
    path('pesquisas/relatorio/', views.relatorio_view, name='relatorio_view'),  # Adicione isso

]
