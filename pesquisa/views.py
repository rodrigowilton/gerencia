# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Pesquisa
from .forms import  PesquisaForm
from django.db.models import Count, Q, F, FloatField
import matplotlib.pyplot as plt
import io
import urllib, base64
from matplotlib.figure import Figure


def gerencia(request):
    return render(request, 'pesquisas/gerencia.html')

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


def sexo_pie_chart2(request):
    # Calcular percentagem de sexo por bairro
    total_counts = Pesquisa.objects.values('bairro').annotate(
        total=Count('id'),
        masculino=Count('id', filter=Q(sexo='M')),
        feminino=Count('id', filter=Q(sexo='F')),
    )

    for count in total_counts:
        count['percent_masculino'] = (count['masculino'] / count['total']) * 100
        count['percent_feminino'] = (count['feminino'] / count['total']) * 100

    # Renderizar o template com a tabela
    return render(request, 'pesquisas/sexo_pie_chart2.html', {'total_counts': total_counts})

def candidato_list(request):
	candidatos = Candidato.objects.all()
	return render(request, 'candidatos/candidato_list.html', {'candidatos': candidatos})

def idade_pie_chart(request):
    # Contagem de idades
    idade_counts = Pesquisa.objects.values('idade').annotate(count=Count('idade'))

    # Dados do gráfico
    labels = [idade['idade'] for idade in idade_counts]
    sizes = [idade['count'] for idade in idade_counts]
    explode = [0.1] * len(labels)  # "explode" todas as fatias

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
    return render(request, 'pesquisas/idade_pie_chart.html', {'data': uri})

def idade_por_bairro(request):
    # Contagem de idades por bairro
    total_counts = Pesquisa.objects.values('bairro', 'idade').annotate(
        total=Count('id')
    ).order_by('bairro', 'idade')

    # Obter contagem total por bairro
    bairro_counts = Pesquisa.objects.values('bairro').annotate(total=Count('id'))

    # Converter em um dicionário para fácil acesso
    bairro_total_dict = {bairro['bairro']: bairro['total'] for bairro in bairro_counts}

    # Calcular percentagens
    for count in total_counts:
        bairro_total = bairro_total_dict.get(count['bairro'], 1)
        count['percent'] = (count['total'] / bairro_total) * 100

    # Renderizar o template com a tabela
    return render(request, 'pesquisas/idade_por_bairro.html', {'total_counts': total_counts})


def rede_social_pie_chart(request):
    # Contagem de redes sociais
    redes_sociais_counts = Pesquisa.objects.values('rede_social').annotate(total=Count('id'))

    # Dados do gráfico
    labels = [item['rede_social'] for item in redes_sociais_counts]
    sizes = [item['total'] for item in redes_sociais_counts]
    explode = [0.1 if i == max(sizes) else 0 for i in sizes]  # "explode" the slice with the highest value

    # Mapear os códigos das redes sociais para seus nomes completos
    redes_sociais_labels = {
        'FB': 'Facebook',
        'WA': 'WhatsApp',
        'IG': 'Instagram',
        'TW': 'Twitter',
        'YT': 'YouTube',
        'OT': 'Outros',
    }
    labels = [redes_sociais_labels.get(label, label) for label in labels]

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
    return render(request, 'pesquisas/rede_social_pie_chart.html', {'data': uri})

# views.py

from django.shortcuts import render
from django.db.models import Count, Q, F
from .models import Pesquisa

def rede_social_por_bairro(request):
    # Contagem de redes sociais por bairro
    total_counts = Pesquisa.objects.values('bairro').annotate(
        total=Count('id'),
        facebook=Count('id', filter=Q(rede_social='FB')),
        whatsapp=Count('id', filter=Q(rede_social='WA')),
        instagram=Count('id', filter=Q(rede_social='IG')),
        twitter=Count('id', filter=Q(rede_social='TW')),
        youtube=Count('id', filter=Q(rede_social='YT')),
        outros=Count('id', filter=Q(rede_social='OT'))
    )

    for count in total_counts:
        count['percent_facebook'] = (count['facebook'] / count['total']) * 100
        count['percent_whatsapp'] = (count['whatsapp'] / count['total']) * 100
        count['percent_instagram'] = (count['instagram'] / count['total']) * 100
        count['percent_twitter'] = (count['twitter'] / count['total']) * 100
        count['percent_youtube'] = (count['youtube'] / count['total']) * 100
        count['percent_outros'] = (count['outros'] / count['total']) * 100

    # Renderizar o template com a tabela
    return render(request, 'pesquisas/rede_social_por_bairro.html', {'total_counts': total_counts})


def vereador_pie_chart(request):
    pesquisas = Pesquisa.objects.values('vereador').annotate(count=Count('vereador'))

    labels = []
    sizes = []

    for pesquisa in pesquisas:
        vereador_id = pesquisa['vereador']
        if vereador_id:
            labels.append(dict(Pesquisa.VEREADOR_CHOICES).get(vereador_id, vereador_id))
            sizes.append(pesquisa['count'])
        else:
            labels.append('Nenhum')
            sizes.append(pesquisa['count'])

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + string.decode('utf-8')
    buf.close()

    return render(request, 'pesquisas/vereador_pie_chart.html', {'data': uri})


def vereador_por_bairro(request):
    pesquisas = Pesquisa.objects.all()
    bairros = {}
    total_por_bairro = {}

    for pesquisa in pesquisas:
        bairro = pesquisa.bairro
        vereador = pesquisa.vereador

        if bairro not in bairros:
            bairros[bairro] = {v: {"quantidade": 0, "percent": 0} for v in set(pesquisas.values_list('vereador', flat=True))}
            total_por_bairro[bairro] = 0

        if vereador:
            bairros[bairro][vereador]["quantidade"] += 1
            total_por_bairro[bairro] += 1

    for bairro, counts in bairros.items():
        for vereador, data in counts.items():
            if total_por_bairro[bairro] > 0:
                data["percent"] = (data["quantidade"] / total_por_bairro[bairro]) * 100

    context = {
        "bairros": bairros,
        "vereadores": sorted(bairros[list(bairros.keys())[0]].keys()) if bairros else [],
    }

    return render(request, "pesquisas/vereador_por_bairro.html", context)


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


def relatorio_view(request):
    # Gere o relatório
    bairro_counts = Pesquisa.objects.values('bairro').annotate(count=Count('bairro')).order_by('bairro')

    # Renderize o template do relatório
    return render(request, 'pesquisas/relatorio.html', {'bairro_counts': bairro_counts})

def pesquisa_view(request):
	if request.method == 'POST':
		form = PesquisaForm(request.POST)
		if form.is_valid():
			form.save()  # Salva o formulário

			# Gera o relatório
			bairro_counts = Pesquisa.objects.values('bairro').annotate(count=Count('bairro')).order_by('bairro')

			# Renderiza o relatório
			return render(request, 'pesquisas/relatorio.html', {'bairro_counts': bairro_counts})
	else:
		form = PesquisaForm()

	return render(request, 'pesquisas/pesquisa_form.html', {'form': form})
