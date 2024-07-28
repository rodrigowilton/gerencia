# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Candidato, Pesquisa
from .forms import CandidatoForm, PesquisaForm
from django.db.models import Count
from matplotlib.figure import Figure
import io
import urllib, base64
import matplotlib.pyplot as plt



def sexo_pie_chart(request):
    # Contagem de sexo
    masculino_count = Pesquisa.objects.filter(sexo='M').count()
    feminino_count = Pesquisa.objects.filter(sexo='F').count()

    # Dados do gráfico
    labels = 'Masculino', 'Feminino'
    sizes = [masculino_count, feminino_count]
    explode = (0.1, 0)  # "explode" the 1st slice (Masculino)

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # Salvar o gráfico em um buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    # Renderizar o template com o gráfico
    return render(request, 'pesquisas/sexo_pie_chart.html', {'data': uri})

def candidato_list(request):
	candidatos = Candidato.objects.all()
	return render(request, 'candidatos/candidato_list.html', {'candidatos': candidatos})


def candidato_create(request):
	if request.method == 'POST':
		form = CandidatoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('candidato_list')
	else:
		form = CandidatoForm()
	return render(request, 'candidatos/candidato_form.html', {'form': form})


def pesquisa_list(request):
	bairro_counts = Pesquisa.objects.values('bairro').annotate(count=Count('bairro')).order_by('bairro')
	return render(request, 'pesquisas/relatorio.html', {'bairro_counts': bairro_counts})


def pesquisa_create(request):
	if request.method == 'POST':
		form = PesquisaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('pesquisa_success')
	else:
		form = PesquisaForm()
	
	return render(request, 'pesquisas/pesquisa_form.html', {'form': form})


def pesquisa_success(request):
	return render(request, 'pesquisas/pesquisa_success.html')


def pesquisa_view(request):
	if request.method == 'POST':
		form = PesquisaForm(request.POST)
		if form.is_valid():
			form.save()  # Salva o formulário
			
			# Gera o relatório
			bairro_counts = Pesquisa.objects.values('bairro').annotate(count=Count('bairro')).order_by('bairro')
			
			# Renderiza o relatório
			return render(request, 'relatorio.html', {'bairro_counts': bairro_counts})
	else:
		form = PesquisaForm()
	
	return render(request, 'pesquisas/pesquisa_form.html', {'form': form})
