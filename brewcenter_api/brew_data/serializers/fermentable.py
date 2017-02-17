from rest_framework import serializers
from brew_data.models.fermentable import FermentableType, Fermentable

class FermentableTypeSerializer(serializers.ModelSerializer):
    """Simple FermentableType Serializer"""
    class Meta:
        model = FermentableType
        fields = ('id', 'name', 'abbreviation')

class SimpleFermentableSerializer(serializers.ModelSerializer):
    """A simple serializer for fermentables"""
    class Meta:
        model = Fermentable
        fields = (
            'id',
            'name',
            'type_id',
            'country_id', 
            'ppg',
            'lovibond'
        )