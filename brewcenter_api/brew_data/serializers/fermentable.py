from rest_framework import serializers
from brew_data.models import FermentableType, Fermentable, FermentableInstance


class FermentableTypeSerializer(serializers.ModelSerializer):
    """Simple FermentableType Serializer"""
    class Meta:
        model = FermentableType
        fields = ('id', 'name', 'abbreviation')

class FermentableInstanceSerializer(serializers.ModelSerializer):
    """Serializes a single fermentable instance object"""
    class Meta:
        model = FermentableInstance
        fields = (
            'id',
            'year',
            'color',
            'color_units',
            'ppg',
            'ppg',
            'dry_yield_percent',
            'dry_yield_fine_grind_percent',
            'moisture_percent',
            'diastatic_power_lintner',
            'protein_percent',
            'soluble_protein_percent',
            'nitrogen_percent',
        )

class FermentableSerializer(serializers.ModelSerializer):
    """A simple serializer for fermentables"""
    type = FermentableTypeSerializer()
    instances = serializers.ListSerializer(child=FermentableInstanceSerializer())

    class Meta:
        model = Fermentable
        fields = (
            'id',
            'name',
            'type',
            'country',
            'instances',
            'notes'
        )
