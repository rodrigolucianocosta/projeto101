from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class Pessoa(models.Model):
#	matricula = models.AutoField()
	primeiro_nome = models.CharField(max_length=30)
	sobrenome     = models.CharField(max_length=60)
	data_nascimento = models.DateField(auto_now=False)
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

	class Meta:
		verbose_name = "Paciente"
		verbose_name_plural = "Pacientes"

	def __unicode__(self):
		return u"%s %s "%(self.primeiro_nome, self.sobrenome)

#medico herda os atributos de Pessoa
class Medico(Pessoa):
	crm = models.IntegerField()
	especialidade = models.CharField(max_length=20)

	class Meta:
		verbose_name = "Medico"
		verbose_name_plural = "Medicos"

	def __unicode__(self):
		return u"%s %s "%(self.primeiro_nome,self.sobrenome)

class Consulta(models.Model):
	data_consulta = models.DateField(auto_now=False)
	hora_consulta = models.TimeField(auto_now=False)
	
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
	paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
	medico   = models.OneToOneField(Medico,   on_delete=models.CASCADE)
	observacoes = models.CharField(max_length=100,blank=True, null=True)
	
	
	class Meta:
		verbose_name = "Consulta"
		verbose_name_plural = "Consultas"

	def __unicode__(self):
		return u"%s %s"%(self.medico, self.paciente)

	
