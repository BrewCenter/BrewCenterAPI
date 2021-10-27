import graphene
from graphene_django import DjangoObjectType

from ingredients.models import FermentableType

class FermentableTypeNode(DjangoObjectType):
    class Meta:
        model = FermentableType
        fields = ("id", "name", "abbreviation", "is_active")

class Query(graphene.ObjectType):
    fermentable_types = graphene.List(FermentableTypeNode, ids=graphene.List(graphene.String, required=False))

    def resolve_fermentable_type(root, info, id):
        try:
            return FermentableType.objects.get(id)
        except FermentableType.DoesNotExist:
            return None

    def resolve_fermentable_types(root, info, **kwargs):
        if 'id' in kwargs:
            try:
                return FermentableType.objects.get(id)
            except FermentableType.DoesNotExist:
                return None
        if 'ids' in kwargs:
            return FermentableType.objects.filter(id__in=kwargs['ids'])
        return FermentableType.objects.all()

schema = graphene.Schema(query=Query)