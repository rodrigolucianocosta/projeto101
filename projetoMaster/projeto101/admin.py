from django.contrib import admin
from .models import Medico,Consulta,Paciente
# Register your models here.

admin.site.register(Consulta)
admin.site.register(Paciente)
admin.site.register(Medico)
