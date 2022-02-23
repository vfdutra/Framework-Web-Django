from django.shortcuts import render

from django.http import HttpResponse

from .models import Medicos
from .models import Pacientes
from .models import Consultas

# Create your views here.
def home(request):
	return render(request,'home.html')

def medicos(request):
	listaMedicos = Medicos.objects.all()
	return render(request,'listaMedicos.html', {'medicos':listaMedicos})

def pacientes(request):
	listaPacientes = Pacientes.objects.all()
	return render(request,'listaPacientes.html', {'pacientes':listaPacientes})

def consultas(request):
	listaConsultas = Consultas.objects.all()
	return render(request,'listaConsultas.html', {'consultas':listaConsultas})

def verMedico(request, id):
	medico = Medicos.objects.get(id=id)
	consultas = Consultas.objects.all().filter(medico=id)
	return render(request,'verMedico.html', {'medico':medico, 'consultas':consultas})

def verPaciente(request, id):
	paciente = Pacientes.objects.get(id=id)
	consultas = Consultas.objects.all().filter(paciente=id)
	return render(request,'verPaciente.html', {'paciente':paciente, 'consultas':consultas})