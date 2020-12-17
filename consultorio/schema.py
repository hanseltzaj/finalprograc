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

class ConsultaModel(DjangoObjectType):
    class Meta:
        model = Consulta

class NuevaConsulta(graphene.Mutation):
    new = graphene.Field(ConsultaModel)

    class Arguments:
        paciente = graphene.String(required=True)
        sintomas = graphene.String(required=True)
        medicamento =  graphene.String(required=True)

    def mutate(self, info, paciente, sintomas, medicamento):
        new = Consulta(paciente=paciente,sintomas=sintomas,medicamento=medicamento)
        new.save()

        return NuevaConsulta(new = new)

class EditarConsulta(graphene.Mutation):
    new = graphene.Field(ConsultaModel)

    class Arguments:
        paciente = graphene.String(required=True)
        sintomas = graphene.String(required=True)
        medicamento =  graphene.String(required=True)
        id = graphene.String(required=True)

    def mutate(self, info, paciente, sintomas, medicamento, id):
        new = Consulta.objects.get(id=id)
        new.paciente = paciente
        new.sintomas = sintomas
        new.medicamento = medicamento
        new.save()

        return EditarConsulta(new=new)

class EliminarConsulta(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String(required=True)
    
    def mutate (self, info, id):
        new = Consulta.objects.get(id=id)
        new.delete()
        ok = True

        return EliminarConsulta(ok=ok)


class MedicamentoNode(DjangoObjectType):
    class   Meta:
        model = Medicamento
        filter_fields = ['nombre', 'dosis']
        interfaces = (relay.Node,)

class MedicamentoModel(DjangoObjectType):
    class Meta:
        model = Medicamento

class NuevaMedicamento(graphene.Mutation):
    new = graphene.Field(MedicamentoModel)

    class Arguments:
        nombre = graphene.String(required=True)
        dosis = graphene.String(required=True)

    def mutate(self, info, nombre, dosis):
        new = Medicamento(nombre=nombre,dosis=dosis)
        new.save()

        return NuevaMedicamento(new = new)

class EditarMedicamento(graphene.Mutation):
    new = graphene.Field(MedicamentoModel)

    class Arguments:
        nombre = graphene.String(required=True)
        dosis = graphene.String(required=True)
        id = graphene.String(required=True)

    def mutate(self, info, nombre, dosis, id):
        new = Medicamento.objects.get(id=id)
        new.nombre = nombre
        new.dosis = dosis
        new.save()

        return EditarMedicamento(new=new)

class EliminarMedicamento(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String(required=True)
    
    def mutate (self, info, id):
        new = Medicamento.objects.get(id=id)
        new.delete()
        ok = True

        return EliminarMedicamento(ok=ok)

class CitaNode(DjangoObjectType):
    class   Meta:
        model = Cita
        filter_fields = ['paciente','fecha']
        interfaces = (relay.Node,)

class CitaModel(DjangoObjectType):
    class Meta:
        model = Cita

class NuevaCita(graphene.Mutation):
    new = graphene.Field(CitaModel)

    class Arguments:
        fecha = graphene.String(required=True)
        paciente = graphene.String(required=True)
        estado = graphene.String(required=True)

    def mutate(self, info, fecha, paciente, estado):
        new = Cita(fecha=fecha,paciente=paciente, estado=estado)
        new.save()

        return NuevaCita(new = new)

class EditarCita(graphene.Mutation):
    new = graphene.Field(CitaModel)

    class Arguments:
        fecha = graphene.String(required=True)
        paciente = graphene.String(required=True)
        estado = graphene.String(required=True)
        id = graphene.String(required=True)

    def mutate(self, info, fecha, paciente, estado,id):
        new = Cita.objects.get(id=id)
        new.fecha = fecha
        new.paciente = paciente
        new.estado = estado
        new.save()

        return EditarCita(new=new)

class EliminarCita(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String(required=True)
    
    def mutate (self, info, id):
        new = Cita.objects.get(id=id)
        new.delete()
        ok = True

        return EliminarCita(ok=ok)

class PacienteNode(DjangoObjectType):
    class   Meta:
        model = Paciente
        filter_fields = ['nombre','direccion']
        interfaces = (relay.Node,)

class PacienteModel(DjangoObjectType):
    class Meta:
        model = Paciente

class NuevoPaciente(graphene.Mutation):
    new = graphene.Field(PacienteModel)

    class Arguments:
        nombre = graphene.String(required=True)
        fechanacimiento = graphene.String(required=True)
        direccion = graphene.String(required=True)
        telefono = graphene.String(required=True)

    def mutate(self, info, nombre, fechanacimiento, direccion, telefono):
        new = Paciente(nombre=nombre,fechanacimiento=fechanacimiento, direccion=direccion, telefono=telefono)
        new.save()

        return NuevoPaciente(new = new)

class EditarPaciente(graphene.Mutation):
    new = graphene.Field(PacienteModel)

    class Arguments:
        nombre = graphene.String(required=True)
        fechanacimiento = graphene.String(required=True)
        direccion = graphene.String(required=True)
        telefono = graphene.String(required=True)
        id = graphene.String(required=True)

    def mutate(self, info, nombre, fechanacimiento, direccion, telefono,id):
        new = Paciente.objects.get(id=id)
        new.nombre = nombre
        new.fechanacimiento = fechanacimiento
        new.direccion = direccion
        new.telefono = telefono
        new.save()

        return EditarPaciente(new=new)

class EliminarPaciente(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.String(required=True)
    
    def mutate (self, info, id):
        new = Paciente.objects.get(id=id)
        new.delete()
        ok = True

        return EliminarPaciente(ok=ok)

class Query(graphene.ObjectType):
    consulta = relay.Node.Field(ConsultaNode)
    all_consultas = DjangoFilterConnectionField(ConsultaNode)   

    medicamento = relay.Node.Field(MedicamentoNode)
    all_medicamentos = DjangoFilterConnectionField(MedicamentoNode)      

    cita = relay.Node.Field(CitaNode)
    all_citas = DjangoFilterConnectionField(CitaNode)        

    paciente = relay.Node.Field(PacienteNode)
    all_pacientes = DjangoFilterConnectionField(PacienteNode)       

class Mutation(graphene.ObjectType):
    create_consulta = NuevaConsulta.Field()
    update_consulta = EditarConsulta.Field()
    delete_consulta = EliminarConsulta.Field()

    create_medicamento = NuevaMedicamento.Field()
    update_medicamento = EditarMedicamento.Field()
    delete_medicamento = EliminarMedicamento.Field()

    create_cita = NuevaCita.Field()
    update_cita = EditarCita.Field()
    delete_cita = EliminarCita.Field()

    create_paciente = NuevoPaciente.Field()
    update_paciente = EditarPaciente.Field()
    delete_paciente = EliminarPaciente.Field()