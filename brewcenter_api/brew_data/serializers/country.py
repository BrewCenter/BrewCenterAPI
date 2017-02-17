from rest_framework import serializers
from brew_data.models.country_code import CountryCode

class CountryCodeSerializer(serializers.ModelSerializer):
    """A simple serializer for fermentables"""
    class Meta:
        model = CountryCode
        fields = ('id','code')
