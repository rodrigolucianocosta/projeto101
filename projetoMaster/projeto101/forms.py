from django import forms
from models import Medico,Paciente,Consulta

class PacienteForm(forms.ModelForm):
	class Meta:
		model = Paciente
		fields = ['sintomas','prontuario']
	
class NameForm(forms.Form):
	marvelous = forms.CharField(label='nome de usuario', max_length=100)

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)
	sender  = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)
