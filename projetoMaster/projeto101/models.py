from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pessoa(models.Model):
	#matricula
	primeiro_nome = models.CharField(max_length=30)
	sobrenome     = models.CharField(max_length=60)
	#rua
	#numero
	#bairro
	#cidade
	#estado
	#telefone
	#email

#paciente herda os atributos de Pessoa
class Paciente(Pessoa):
	#cartao_sus
	sintomas = models.CharField(max_length=100)
	prontuario = models.CharField(max_length=100)

#medico herda os atributos de Pessoa
class Medico(Pessoa):
	crm = models.IntegerField()
	especialidade = models.CharField(max_length=20)

class Consulta(models.Model):
	prioridade = (
	('AL','Alta'),
	('MD', 'Media'),
	('BX', 'Baixa'),
	)
#------------------------------------------------------------------
	tipo_atendimento = (
	('AG', 'Agendamento'),
	('RT', 'Retorno'),
	('EM', 'Emergencial'),
	)
#------------------------------------------------------------------
	paciente = models.OneToOneField(Paciente)
	medico   = models.OneToOneField(Medico)
	observacoes = models.CharField(max_length=100,default='DEFAULT VALUE',blank=True, null=True
)


	
