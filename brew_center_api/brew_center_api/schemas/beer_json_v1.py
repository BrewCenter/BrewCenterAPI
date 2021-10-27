import graphene
from graphene_django import DjangoObjectType
from ingredients.models import FermentableBase

def self_resolver(object, query_info):
    return object

def create_nested_attr_resolver(*args):
    def resolver(object, info):
        value = object
        for attr in args:
            if value and getattr(value, attr):
                value = getattr(value, attr)
            else:
                value = None
        return value
    return resolver

def ppg_to_sg(ppg_value):
    """
    Converts ppg (Points Per Gallon) which is a measure of how many specific gravity
    points you would have if you disolved a fermentable in one gallon of water, into Specific Gravity.

    A PPG value ranges from 0 to 46 (46 being the PPG of Sucrose).
    The SG value for a PPG of 46 is 1.046.

    Params:
    - ppg_value: Number
    """
    return 1.0 + (ppg_value / 1000)

def calc_grind_fermentability_percent(grind_ppg, potential_ppg):
    if not grind_ppg or not potential_ppg:
        return None
    return grind_ppg / potential_ppg

class AcidityPHNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(self, info):
        return 'pH'

    def resolve_value(value, info):
        return value

class ConcentrationPPMNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(self, info):
        return 'ppm'

    def resolve_value(value, info):
        return value

class ViscosityCPNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(self, info):
        return 'cP'

    def resolve_value(value, info):
        return value

class PercentageNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(self, info):
        return '%'

    def resolve_value(value, info):
        return value * 100

class SpecificGravityNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(self, info):
        return 'sg'

    def resolve_value(value, info):
        return value


class LintnerNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(self, info):
        return 'Lintner'

    def resolve_value(value, info):
        return value

class SRMColorNode(graphene.ObjectType):
    unit = graphene.String()
    value = graphene.Float()

    def resolve_unit(*args):
        return 'srm'

    def resolve_value(color_srm, info):
        return color_srm

class YieldNode(graphene.ObjectType):
    fine_grind = graphene.Field(PercentageNode)
    coarse_grind = graphene.Field(PercentageNode)
    fine_coarse_difference = graphene.Field(PercentageNode)
    potential = graphene.Field(SpecificGravityNode, source='potential_ppg')

    def resolve_fine_grind(fermentable, info):
        if not fermentable.grain:
            return None
        
        return calc_grind_fermentability_percent(
            fermentable.grain.fine_grind_potential_ppg,
            fermentable.potential_ppg
        )

    def resolve_coarse_grind(fermentable, info):
        if not fermentable.grain:
            return None
        
        return calc_grind_fermentability_percent(
            fermentable.grain.coarse_grind_potential_ppg,
            fermentable.potential_ppg
        )

    def resolve_fine_coarse_difference(fermentable, info):
        if not fermentable.grain:
            return None
        
        fine_grind_percent = calc_grind_fermentability_percent(
            fermentable.grain.fine_grind_potential_ppg,
            fermentable.potential_ppg
        )
        coarse_grind_percent = calc_grind_fermentability_percent(
            fermentable.grain.coarse_grind_potential_ppg,
            fermentable.potential_ppg
        )
        difference = fine_grind_percent - coarse_grind_percent
        return difference

class FermentableNode(DjangoObjectType):
    class Meta:
        model = FermentableBase
        fields = (
            "id",
            "name",
            "type",
            "notes",
            "potential_ppg",
            "notes"
        )

    # Fields on the FermentableBase model
    producer_id = graphene.Field(graphene.String, source='product_id')
    fermentability = graphene.Field(PercentageNode, source='fermentability_percent')
    producer = graphene.String(resolver=create_nested_attr_resolver('manufacturer', 'name'))
    origin = graphene.String(resolver=create_nested_attr_resolver('origin', 'name'))
    color = graphene.Field(SRMColorNode, source='color_srm')
    grain_group = graphene.String(resolver=create_nested_attr_resolver('grain', 'type', 'name'))

    # Fields from the Grain sub-model
    yield_sg = graphene.Field(YieldNode, name='yield', resolver=lambda ferm, info : ferm)
    moisture = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'moisture_percent'))
    alpha_amylase = graphene.Float(resolver=create_nested_attr_resolver('grain', 'alpha_amylase'))
    diastatic_power = graphene.Field(LintnerNode, resolver=create_nested_attr_resolver('grain', 'diastatic_power_lintner'))
    protein = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'protein_percent'))
    kolbach_index = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'kolbach_index_percent'))
    max_in_batch = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'max_in_batch_percent'))
    recommend_mash = graphene.Boolean(resolver=create_nested_attr_resolver('grain', 'recommend_mash'))
    glassy = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'glassy_percent'))
    plump = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'plump_percent'))
    mealy = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'mealy_percent'))
    thru = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'thru_percent'))
    glassy = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'glassy_percent'))
    friability = graphene.Field(PercentageNode, resolver=create_nested_attr_resolver('grain', 'friability_percent'))
    di_ph = graphene.Field(AcidityPHNode, resolver=create_nested_attr_resolver('grain', 'di_ph'))
    viscosity = graphene.Field(ViscosityCPNode, resolver=create_nested_attr_resolver('grain', 'viscosity_cp'))
    dms_p = graphene.Field(ConcentrationPPMNode, resolver=create_nested_attr_resolver('grain', 'dms_precursors_ppm'))
    fan = graphene.Field(ConcentrationPPMNode, resolver=create_nested_attr_resolver('grain', 'fan_ppm'))
    beta_glucan = graphene.Field(ConcentrationPPMNode, resolver=create_nested_attr_resolver('grain', 'beta_glucan_ppm'))

class Query(graphene.ObjectType):
    version = graphene.String()
    fermentables = graphene.List(
        FermentableNode, ids=graphene.List(graphene.String, required=False))

    def resolve_version(*args):
        return '1.0'

    def resolve_fermentables(root, info, **kwargs):
        if 'ids' in kwargs:
            return FermentableBase.objects.filter(id__in=kwargs['ids'])
        return FermentableBase.objects.all()


schema = graphene.Schema(query=Query, auto_camelcase=False)