from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('send', views.send, name='send'),
	path('lookup', views.lookup, name='lookup'),
]
