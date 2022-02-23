from django.db import models

# Create your models here.
class Pacientes(models.Model):
	nome = models.CharField(max_length=100,verbose_name="Nome do Paciente")
	cpf = models.CharField(max_length=20,verbose_name="CPF do Paciente")
	email = models.CharField(max_length=100,verbose_name="Email do Paciente")
	telefone = models.CharField(max_length=20,verbose_name="Telefone do Paciente")
	endereco = models.CharField(max_length=100,verbose_name="Endereço do Paciente")
	idade = models.CharField(max_length=3,verbose_name="Idade do Paciente")
	def __str__(self):
		return self.nome

class Medicos(models.Model):
	nome = models.CharField(max_length=100,verbose_name="Nome do Médico")
	cpf = models.CharField(max_length=20,verbose_name="CPF do Médico")
	email = models.CharField(max_length=100,verbose_name="Email do Médico")
	telefone = models.CharField(max_length=20,verbose_name="Telefone do Médico")
	crm = models.CharField(max_length=10,verbose_name="CRM do Médico")
	especialidade = models.CharField(max_length=100,verbose_name="Especialidade do Médico")
	def __str__(self):
		return self.nome

class Consultas(models.Model):
	medico = models.ForeignKey(Medicos, on_delete=models.PROTECT)
	paciente = models.ForeignKey(Pacientes, on_delete=models.PROTECT)
	data = models.DateTimeField(verbose_name="Data da Consulta")
	convenio = models.CharField(max_length=20,verbose_name="Convênio")
	valor = models.CharField(max_length=10,verbose_name="Valor da Consulta")
	def __str__(self):
		return str(self.id)