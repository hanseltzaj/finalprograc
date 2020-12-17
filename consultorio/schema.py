import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from consultorio.models import Consulta, Medicamento, Cita, Paciente

class ConsultaNode(DjangoObjectType):
    class Meta:
        model = Consulta
        filter_fields = ['fecha_creacion','paciente']
        interfaces = (relay.Node, )

class MedicamentoNode(DjangoObjectType):
    class   Meta:
        model = Medicamento
        filter_fields = ['nombre', 'dosis']
        interfaces = (relay.Node,)

class CitaNode(DjangoObjectType):
    class   Meta:
        model = Cita
        filter_fields = ['paciente','fecha']
        interfaces = (relay.Node,)

class PacienteNode(DjangoObjectType):
    class   Meta:
        model = Paciente
        filter_fields = ['nombre','direccion']
        interfaces = (relay.Node,)

        