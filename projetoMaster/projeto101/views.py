from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader

from .models import Consulta,Paciente,Medico


# Create your views here
#def index(request):
#	latest_name_list = Paciente.objects.all()
#	output = ', '.join([p.sobrenome for p in latest_name_list])
#	return HttpResponse(output)
#reescrevendo usando templates

def index(request):
	latest_name_list = Paciente.objects.order_by('data_nascimento')[:5]
#	template = loader.get_template('index.html')
	context = {'latest_name_list': latest_name_list,}
#	return HttpResponse(template.render(context, request))
	return render(request, 'index.html', context)

def detail(request, paciente_id):
	try:
		paciente = Paciente.objects.get(pk=paciente_id)
	except Paciente.DoesNotExist:
		raise Http404("Paciente does not exist")
#	return HttpResponse("you are in the paciente %s" % paciente_id)
	return render(request,'detail.html', {'paciente':paciente})

	
def results(request, paciente_id):
	response = 'you are in the results of paciente %s'
	return HttpResponse(response % paciente_id)
