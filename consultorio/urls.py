from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url('consultorio/pacientes/', views.paciente_lista, name='paciente_lista'),
    path('consultorio/consultas/', views.consulta_lista, name='consulta_lista'),
]
