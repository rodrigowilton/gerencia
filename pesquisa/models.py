from django.db import models



class Candidato(models.Model):
	nome = models.CharField(max_length=100)
	
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
	
	PESQUISADORA_CHOICES = [
		('P1', 'Pesquisador 1'),
		('P2', 'Pesquisador 2'),
		('P3', 'Pesquisador 3'),
		('P4', 'Pesquisador 4'),
		('P5', 'Pesquisador 5'),
		('P6', 'Pesquisador 6'),
	]
	VEREADOR_INDUZIDO_CHOICES = [
		('FM', 'Felipe Michel'),
		('KB', 'Kaio Brazao'),
		('CC', 'Carlos Caiado'),
		('LC', 'Luiz Carlos'),
		('RC', 'Ramos Filho'),
		('NS', 'Não Sabe'),
	]

	CIDADE_CHOICES = [
		('NI', 'Nova Iguaçu'),
	]

	BAIRRO_CHOICES = [
		('TP', 'Tropical'),
		('ML', 'Monte Libano'),
		('PT', 'Prata'),
	]

	cidade = models.CharField(max_length=2, choices=CIDADE_CHOICES)
	pesquisadora = models.CharField(max_length=2, choices=PESQUISADORA_CHOICES)
	bairro = models.CharField(max_length=2, choices=BAIRRO_CHOICES)
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
	idade = models.CharField(max_length=5, choices=IDADE_CHOICES)
	votaria_brazao = models.CharField(max_length=1, choices=VOTARIA_CHOICES)
	vereador = models.ForeignKey(
		Candidato,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name='pesquisas_prefeito'  # Opcional, define o nome da relação reversa
	)
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
	
	data = models.DateTimeField(auto_now_add=True)  # Exemplo de campo de data
	
	def __str__(self):
		return f'{self.cidade} - {self.bairro}'
