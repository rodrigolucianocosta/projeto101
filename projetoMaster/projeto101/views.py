from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .forms import NameForm

# Create your views here.
def get_name(request):
	#if this is a POST request we need to process the form data
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = NameForm(request.POST)
		#check whether it's valid:
		if form.is_valid():
		#process data in form.cleaned_data as required
		#..
		# redirect to a new url
			return HttpResponseRedirect('/thanks/')
	#if a GET (or any other method ) we will create a blank form
	else:
		form = NameForm()

	return render(request, 'index.html', {'form':form})

def medico(request):
	return render(request, 'medico.html')


def contact(request):
	if form.is_valid():
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
		sender  = form.cleaned_data['sender']
		cc_myself = form.cleaned_data['cc_myself']

		recipients = ['rodrigolucianocosta@gmail.com']
		if cc_myself:
			recipients.append(sender)
		send_mail(subject, message, sender, recipients)
		return HttpResponseRedirect('/thanks/')
