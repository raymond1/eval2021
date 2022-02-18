from django.urls import path, include
from . import views

urlpatterns = [
  path('lookup/<str:address>/', views.lookup, name='lookup'),
  path('generate_qr_code/<str:address>', views.generate_qr_code, name='generate_qr_code'),
]