from rest_framework import serializers
from brew_data.models import YeastType, Yeast


class YeastTypeSerializer(serializers.ModelSerializer):
    """Simple FermentableType Serializer"""
    class Meta:
        model = YeastType
        fields = ('id', 'name')


class SimpleYeastSerializer(serializers.ModelSerializer):
    """A simple serializer for hops"""
    class Meta:
        model = Yeast
        fields = (
            'id',
            'name',
            'type_id',
            'min_temp',
            'max_temp',
            'flocculation',
            'attenuation'
        )
