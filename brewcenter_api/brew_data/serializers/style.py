from rest_framework import serializers
from brew_data.models import Style


class SimpleStyleSerializer(serializers.ModelSerializer):
    """A simple serializer for styles"""
    class Meta:
        model = Style
        fields = (
            'id',
            'name'
        )
