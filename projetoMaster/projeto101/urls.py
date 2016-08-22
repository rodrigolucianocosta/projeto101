from django.conf.urls import url

from . import views

app_name = 'projeto101'
urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^(?P<paciente_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^(?P<paciente_id>[0-9]+)/results/$',views.results, name='results'),
	url(r'^(?P<paciente_id>[0-9]+)/vote/$', views.vote,name='vote'),
	
]
