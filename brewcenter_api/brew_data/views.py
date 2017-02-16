from django.shortcuts import render
from rest_framework import serializers as rf_serializers
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from . import models
from . import serializers

from rest_framework.decorators import api_view

@api_view(['GET'])
def styles(request):
    """Returns all styles in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.Style.objects.all(), child=serializers.SimpleStyleSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def countries(request):
    """Returns all countries in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.CountryCode.objects.all(), child=serializers.CountryCodeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def fermentable_types(request):
    """Returns all fermentables in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.FermentableType.objects.all(), child=serializers.FermentableTypeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def fermentables(request):
    """Returns all fermentables in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.Fermentable.objects.all(), child=serializers.SimpleFermentableSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def hop_types(request):
    """Returns all hop types in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.HopType.objects.all(), child=serializers.HopTypeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def hops(request):
    """Returns all hops in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.Hop.objects.all(), child=serializers.SimpleHopSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def yeast_types(request):
    """Returns all yeast types in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.YeastType.objects.all(), child=serializers.YeastTypeSerializer())
    return Response(serializer.data)

@api_view(['GET'])
def yeast(request):
    """Returns all yeast in the system as JSON"""
    serializer = rf_serializers.ListSerializer(models.Yeast.objects.all(), child=serializers.SimpleYeastSerializer())
    return Response(serializer.data)