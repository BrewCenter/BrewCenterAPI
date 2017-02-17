from django.shortcuts import render
from rest_framework import serializers as rf_serializers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from brew_data.models.country_code import CountryCode
from brew_data.models.style import Style
from brew_data.models.fermentable import Fermentable, FermentableType
from brew_data.models.hop import Hop, HopType
from brew_data.models.yeast import Yeast, YeastType

from brew_data import serializers

from rest_framework.decorators import api_view

@api_view(['GET'])
def styles(request):
    """Returns all styles in the system as JSON"""
    serializer = rf_serializers.ListSerializer(Style.objects.all(), child=serializers.style.SimpleStyleSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def countries(request):
    """Returns all countries in the system as JSON"""
    serializer = rf_serializers.ListSerializer(CountryCode.objects.all(), child=serializers.country.CountryCodeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def fermentable_types(request):
    """Returns all fermentables in the system as JSON"""
    serializer = rf_serializers.ListSerializer(FermentableType.objects.all(), child=serializers.fermentable.FermentableTypeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def fermentables(request):
    """Returns all fermentables in the system as JSON"""
    serializer = rf_serializers.ListSerializer(Fermentable.objects.all(), child=serializers.fermentable.SimpleFermentableSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def hop_types(request):
    """Returns all hop types in the system as JSON"""
    serializer = rf_serializers.ListSerializer(HopType.objects.all(), child=serializers.hop.HopTypeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def hops(request):
    """Returns all hops in the system as JSON"""
    serializer = rf_serializers.ListSerializer(Hop.objects.all(), child=serializers.hop.SimpleHopSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def yeast_types(request):
    """Returns all yeast types in the system as JSON"""
    serializer = rf_serializers.ListSerializer(YeastType.objects.all(), child=serializers.yeast.YeastTypeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def yeast(request):
    """Returns all yeast in the system as JSON"""
    serializer = rf_serializers.ListSerializer(Yeast.objects.all(), child=serializers.yeast.SimpleYeastSerializer())
    return Response(serializer.data)