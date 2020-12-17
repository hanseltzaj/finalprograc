from django.contrib import admin
from consultorio.models import Paciente, Cita, Medicamento, Consulta

admin.site.register(Paciente)
admin.site.register(Cita)
admin.site.register(Medicamento)
admin.site.register(Consulta)
