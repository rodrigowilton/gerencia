# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Candidato, Pesquisa
from .forms import CandidatoForm, PesquisaForm
from django.db.models import Count


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
