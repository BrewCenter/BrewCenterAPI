from rest_framework import serializers
from brew_data.models.hop import HopType, Hop

class HopTypeSerializer(serializers.ModelSerializer):
    """Simple FermentableType Serializer"""
    class Meta:
        model = HopType
        fields = ('id', 'name')

class SimpleHopSerializer(serializers.ModelSerializer):
    """A simple serializer for hops"""
    class Meta:
        model = Hop
        fields = (
            'id',
            'name',
            'type_id',
            'country_id', 
            'alpha_acids',
            'beta_acids'
        )