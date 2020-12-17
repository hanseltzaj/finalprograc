from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Paciente, Medicamento, Cita, Consulta
from django.utils import timezone
from .forms import PublicacionForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def Paciente_lista(request):
    pacientes = Paciente.objects.filter()
    return render(request, 'consultorio/paciente_lista.html', {'pacientes':pacientes})

def Cita_lista(request):
    citas = Cita.objects.filter(fecha__lte=timezone.now()).order_by('fecha')
    return render(request, 'consultorio/cita_lista.html', {'citas':citas})

def Medicamento_lista(request):
    medicamentos = Medicamento.objects.filter()
    return render(request, 'consultorio/medicamento_lista.html', {'medicamentos':medicamentos})

def Consulta_lista(request):
    consultas = Consulta.objects.filter()
    return render(request, 'consultorio/consulta_lista.html', {'consultas':consultas})

def Paciente_detalle(request, pk):
    paciente = get_object_or_404(paciente, pk=pk)
    return render(request, 'consultorio/paciente_detalle.html', {'paciente':paciente})

def Cita_detalle(request, pk):
    cita = get_object_or_404(cita, pk=pk)
    return render(request, 'consultorio/cita_detalle.html', {'cita':cita})

def Medicamento_detalle(request, pk):
    medicamento = get_object_or_404(medicamento, pk=pk)
    return render(request, 'consultorio/medicamento_detalle.html', {'medicamento':medicamento})

def Consulta_detalle(request, pk):
    consulta = get_object_or_404(consulta, pk=pk)
    return render(request, 'consultorio/consulta_detalle.html', {'consulta':consulta})

@login_required
def Paciente_eliminar(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('paciente_lista')

@login_required
def Medicamento_eliminar(request, pk):
    medicamento = get_object_or_404(Medicamento, pk=pk)
    medicamento.delete()
    return redirect('medicamento_lista')

@login_required
def Cita_eliminar(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    cita.delete()
    return redirect('cita_lista')

@login_required
def Consulta_eliminar(request, pk):
    consulta = get_object_or_404(Consulta, pk=pk)
    consutla.delete()
    return redirect('paciente_lista')

@login_required
def cita_borrador_lista(request):
    citas = Cita.objects.filter(fecha__isnull=True).order_by('fecha')
    return render(request, 'consultorio/cita_borrador_lista.html', {'citas': citas})

@login_required
def cita_atender(request,pk):
    cita = get_object_or_404(Cita, pk=pk)
    cita.atender()
    return redirect('cita_detalle', pk=cita.pk)
