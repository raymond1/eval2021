from django.urls import path, include
from . import views

urlpatterns = [
  path('lookup/<str:address>/', views.lookup, name='lookup')
]