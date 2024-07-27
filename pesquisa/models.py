from django.db import models


class Candidato(models.Model):
	nome = models.CharField(max_length=100)
	cargo = models.CharField(max_length=20, choices=[('Prefeito', 'Prefeito'), ('Vereador', 'Vereador')])
	
	def __str__(self):
		return self.nome


class Pesquisa(models.Model):
	SEXO_CHOICES = [
		('M', 'Masculino'),
		('F', 'Feminino'),
	]
	
	IDADE_CHOICES = [
		('16-25', '16 a 25 anos'),
		('26-34', '26 a 34 anos'),
		('35-55', '35 a 55 anos'),
		('55+', 'Acima de 55 anos'),
	]
	
	VOTARIA_CHOICES = [
		('S', 'Sim'),
		('N', 'Não'),
	]
	
	VOTARIA_PRESIDENTE_CHOICES = [
		('LL', 'LULA'),
		('BS', 'BOLSONARO'),
	]
	
	REDES_SOCIAIS_CHOICES = [
		('FB', 'Facebook'),
		('WA', 'WhatsApp'),
		('IG', 'Instagram'),
		('TW', 'Twitter'),
		('YT', 'YouTube'),
		('OT', 'Outros'),
	]
	VEREADOR_INDUZIDO_CHOICES = [
		('FM', 'Felipe Michel'),
		('KB', 'Kaio Brazao'),
		('CC', 'Carlos Caiado'),
		('LC', 'Luiz Carlos'),
		('RC', 'Ramos Filho'),
		('NS', 'Não Sabe'),
	]
	
	cidade = models.CharField(max_length=100)
	pesquisadora = models.CharField(max_length=100)
	bairro = models.CharField(max_length=100)
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
	idade = models.CharField(max_length=5, choices=IDADE_CHOICES)
	votaria_brazao = models.CharField(max_length=1, choices=VOTARIA_CHOICES)
	prefeito = models.ForeignKey(Candidato, on_delete=models.SET_NULL, null=True, blank=True,
								 limit_choices_to={'cargo': 'Prefeito'}, related_name='pesquisas_prefeito')
	rede_social = models.CharField(max_length=2, choices=REDES_SOCIAIS_CHOICES)
	prioridade_prefeito = models.CharField(max_length=100)
	politico_mais_fez = models.CharField(max_length=100)
	votaria_presidente = models.CharField(max_length=2, choices=VOTARIA_PRESIDENTE_CHOICES)
	
	vereador_induzido = models.CharField(max_length=2, choices=VEREADOR_INDUZIDO_CHOICES)
	
	
	vereador_espontaneo_1 = models.CharField(max_length=100, blank=True, null=True)
	vereador_espontaneo_2 = models.CharField(max_length=100, blank=True, null=True)
	vereador_espontaneo_3 = models.CharField(max_length=100, blank=True, null=True)
	vereador_espontaneo_4 = models.CharField(max_length=100, blank=True, null=True)
	vereador_espontaneo_5 = models.CharField(max_length=100, blank=True, null=True)
	vereador_espontaneo_6 = models.CharField(max_length=100, blank=True, null=True)
	
	def __str__(self):
		return f"Pesquisa {self.id} - {self.cidade}"