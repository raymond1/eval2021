from django.urls import path
from . import views

app_name = 'send'
urlpatterns = [
	path('', views.index, name='index'),
	path('send', views.send, name='send'),
	path('lookup/<str:address>', views.lookup, name='lookup'),
	path('lookup', views.lookup, name='lookup'),
]
