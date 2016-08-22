from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.template import loader

from .models import Consulta,Paciente,Medico


def index(request):
	return render_to_response('index.html')


def detail(request, paciente_id):
#	try:
#		paciente = Paciente.objects.get(pk=paciente_id)
#	except Paciente.DoesNotExist:
#		raise Http404("Paciente does not exist")
#	return HttpResponse("you are in the paciente %s" % paciente_id)
#	return render(request,'detail.html', {'paciente':paciente})
	paciente = get_object_or_404(Paciente, pk=paciente_id)
	return render(request, 'detail.html', {'paciente':paciente})
	
def results(request, paciente_id):
	response = 'you are in the results of paciente %s'
	return HttpResponse(response % paciente_id)

def vote(request, pessoa_id):
	pessoa = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = pessoa.choice_set.get(pk=request.POST['primeiro_nome'])
	except (Keyerror, Pessoa.DoesNotExist):
		#Redisplay the pessoa voting form
		return render(request, 'projeto101/detail.html',{
			'pessoa':pessoa,
			'erro_message':"you didn't select a choice",
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		# always return an HttpResponseRedirect after sucessfull dealing
		# with POST data. This prevent data from being posted twice is a
		# user hits the back button
		return HttpResponseRedirect(reverse('projeto101:results', args=(pessoa.id,)))
