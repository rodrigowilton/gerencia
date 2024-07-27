from django import forms
from .models import Pesquisa, Candidato


class CandidatoForm(forms.ModelForm):
	class Meta:
		model = Candidato
		fields = ['nome']
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['nome'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nome do Candidato'})


class PesquisaForm(forms.ModelForm):
	SEXO_CHOICES = [('', 'Escolha'), ('M', 'Masculino'), ('F', 'Feminino')]
	IDADE_CHOICES = [('', 'Escolha'), ('16-25', '16 a 25 anos'), ('26-34', '26 a 34 anos'),
					 ('35-55', '35 a 55 anos'), ('55+', 'Acima de 55 anos')]
	VOTARIA_CHOICES = [('', 'Escolha'), ('S', 'Sim'), ('N', 'Não')]
	REDES_SOCIAIS_CHOICES = [('', 'Escolha'), ('FB', 'Facebook'), ('WA', 'WhatsApp'),
							 ('IG', 'Instagram'), ('TW', 'Twitter'), ('YT', 'YouTube'),
							 ('OT', 'Outros')]
	
	VEREADOR_INDUZIDO_CHOICES = [
		('FM', 'Felipe Michel'),
		('KB', 'Kaio Brazao'),
		('CC', 'Carlos Caiado'),
		('LC', 'Luiz Carlos'),
		('RC', 'Ramos Filho'),
		('NS', 'Não Sabe'),
	]
	
	VOTARIA_PRESIDENTE_CHOICES = [('', 'Escolha'), ('LL', 'LULA'), ('BS', 'BOLSONARO')]
	
	sexo = forms.ChoiceField(choices=SEXO_CHOICES, required=False)
	idade = forms.ChoiceField(choices=IDADE_CHOICES, required=False)
	votaria_brazao = forms.ChoiceField(choices=VOTARIA_CHOICES, required=False)
	vereador = forms.ModelMultipleChoiceField(
		queryset=Candidato.objects.filter(cargo='Vereador'),
		required=False,
		widget=forms.CheckboxSelectMultiple
	)
	rede_social = forms.ChoiceField(choices=REDES_SOCIAIS_CHOICES, required=False)
	prioridade_prefeito = forms.ChoiceField(choices=[('', 'Escolha')] +
													[(opcao, opcao) for opcao in
													 ['Saúde', 'Educação', 'Segurança', 'Infraestrutura',
													  'Transporte', 'Habitação', 'Meio Ambiente',
													  'Cultura', 'Economia', 'Outros']])
	politico_mais_fez = forms.CharField(max_length=100, required=False)
	votaria_presidente = forms.ChoiceField(choices=VOTARIA_PRESIDENTE_CHOICES, required=False)
	
	vereador_induzido = forms.ChoiceField(choices=VEREADOR_INDUZIDO_CHOICES, required=False)
	
	vereador_espontaneo_1 = forms.CharField(max_length=100, required=False)
	vereador_espontaneo_2 = forms.CharField(max_length=100, required=False)
	vereador_espontaneo_3 = forms.CharField(max_length=100, required=False)
	vereador_espontaneo_4 = forms.CharField(max_length=100, required=False)
	vereador_espontaneo_5 = forms.CharField(max_length=100, required=False)
	vereador_espontaneo_6 = forms.CharField(max_length=100, required=False)
	vereador_espontaneo_7 = forms.CharField(max_length=100, required=False)
	
	class Meta:
		model = Pesquisa
		fields = [
			'cidade', 'pesquisadora', 'bairro', 'sexo', 'idade',
			'votaria_brazao', 'prefeito', 'vereador',
			'rede_social', 'prioridade_prefeito', 'politico_mais_fez', 'votaria_presidente',
			'vereador_induzido', 'vereador_espontaneo_1', 'vereador_espontaneo_2',
			'vereador_espontaneo_3', 'vereador_espontaneo_4', 'vereador_espontaneo_5',
			'vereador_espontaneo_6', 'vereador_espontaneo_7'
		]
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['vereador_induzido'].widget.attrs.update({'class': 'form-control'})
		self.fields['vereador_induzido'].required = False