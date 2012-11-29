from django.conf.urls import patterns, include, url
from problems import views

urlpatterns = patterns('',
		url(r'^$', views.index, name='index'),
		url(r'^(?P<problem_id>[0-9]+)$', views.showproblem, 
			name='showproblem'),
		url(r'^(?P<problem_id>[0-9]+)/submit$', views.submit, name='submit')
)
