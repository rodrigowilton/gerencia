from django import forms
from .models import Pesquisa, Candidato


class CandidatoForm(forms.ModelForm):
	class Meta:
		model = Candidato
		fields = '__all__'  # Inclui todos os campos do modelo Candidato no formulário
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		if 'nome' in self.fields:
			self.fields['nome'].widget.attrs.update({
				'class': 'form-control',  # Adiciona uma classe CSS ao widget
				'placeholder': 'Nome do Candidato'  # Adiciona um placeholder
			})


class PesquisaForm(forms.ModelForm):
	SEXO_CHOICES = [('', 'Escolha'), ('M', 'Masculino'), ('F', 'Feminino')]
	
	IDADE_CHOICES = [('', 'Escolha'), ('16-25', '16 a 25 anos'), ('26-34', '26 a 34 anos'),
					 ('35-55', '35 a 55 anos'), ('55+', 'Acima de 55 anos')]
	VOTARIA_CHOICES = [('', 'Escolha'), ('S', 'Sim'), ('N', 'Não')]
	
	REDES_SOCIAIS_CHOICES = [('', 'Escolha'), ('FB', 'Facebook'), ('WA', 'WhatsApp'),
							 ('IG', 'Instagram'), ('TW', 'Twitter'), ('YT', 'YouTube'),
							 ('OT', 'Outros')]
	
	VEREADOR_INDUZIDO_CHOICES = [
		('', 'Escolha'),
		('FM', 'Felipe Michel'),
		('KB', 'Kaio Brazao'),
		('CC', 'Carlos Caiado'),
		('LC', 'Luiz Carlos'),
		('RC', 'Ramos Filho'),
		('NS', 'Não Sabe'),
	]
	
	VOTARIA_PRESIDENTE_CHOICES = [('', 'Escolha'), ('LL', 'LULA'), ('BS', 'BOLSONARO')]
	
	PESQUISADORA_CHOICES = [
		('', 'Escolha'),
		('P1', 'Pesquisador 1'),
		('P2', 'Pesquisador 2'),
		('P3', 'Pesquisador 3'),
		('P4', 'Pesquisador 4'),
		('P5', 'Pesquisador 5'),
		('P6', 'Pesquisador 6'),
	]
	
	pesquisadora = forms.ChoiceField(
		choices=PESQUISADORA_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	sexo = forms.ChoiceField(
		choices=SEXO_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	idade = forms.ChoiceField(
		choices=IDADE_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	votaria_brazao = forms.ChoiceField(
		choices=VOTARIA_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	
	prefeito = forms.ModelChoiceField(
		queryset=Candidato.objects.all(),  # Traz todos os candidatos
		required=False,
		empty_label='Escolha',
		widget=forms.Select(attrs={
			'class': 'form-control',
			'placeholder': 'Selecione o Prefeito'  # Placeholder para o dropdown
		})
	)
	
	rede_social = forms.ChoiceField(
		choices=REDES_SOCIAIS_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	prioridade_prefeito = forms.ChoiceField(
		choices=[('', 'Escolha')] +
				[(opcao, opcao) for opcao in
				 ['Saúde', 'Educação', 'Segurança', 'Infraestrutura',
				  'Transporte', 'Habitação', 'Meio Ambiente',
				  'Cultura', 'Economia', 'Outros']],
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	
	politico_mais_fez = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	
	votaria_presidente = forms.ChoiceField(
		choices=VOTARIA_PRESIDENTE_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	
	vereador_induzido = forms.ChoiceField(
		choices=VEREADOR_INDUZIDO_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-control'})
	)
	
	vereador_espontaneo_1 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	vereador_espontaneo_2 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	vereador_espontaneo_3 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	vereador_espontaneo_4 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	vereador_espontaneo_5 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	vereador_espontaneo_6 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	vereador_espontaneo_7 = forms.CharField(
		max_length=100,
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)
	
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
		# Atualiza os widgets para usar a classe 'form-control' e adicionar bordas
		for field_name in self.fields:
			if isinstance(self.fields[field_name], (forms.ChoiceField, forms.ModelChoiceField, forms.CharField)):
				self.fields[field_name].widget.attrs.update({
					'class': 'form-control',
					'style': 'border: 1px solid #ced4da;'  # Adiciona uma borda padrão
				})
