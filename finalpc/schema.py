import graphene
import consultorio.schema

class Query(consultorio.schema.Query, graphene.ObjectType):
    pass
    
class Mutation(consultorio.schema.Mutation, graphene.ObjectType,):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)