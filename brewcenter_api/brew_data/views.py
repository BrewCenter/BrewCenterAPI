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

from rest_framework import viewsets

class StyleViewSet(viewsets.ModelViewSet):
    """Returns All Beer Styles"""
    serializer_class = serializers.style.SimpleStyleSerializer
    queryset = Style.objects.all()

class CountryViewSet(viewsets.ModelViewSet):
    """Returns All Countries"""
    serializer_class = serializers.country.CountryCodeSerializer
    queryset = CountryCode.objects.all()

class FermentableTypeViewSet(viewsets.ModelViewSet):
    """Returns All Fermentable Types"""
    serializer_class = serializers.fermentable.FermentableTypeSerializer
    queryset = FermentableType.objects.all()

class FermentableViewSet(viewsets.ModelViewSet):
    """Returns All Fermentables"""
    serializer_class = serializers.fermentable.SimpleFermentableSerializer
    queryset = Fermentable.objects.all()

class HopTypeViewSet(viewsets.ModelViewSet):
    """Returns All Beer Styles"""
    serializer_class = serializers.hop.HopTypeSerializer
    queryset = HopType.objects.all()

class HopViewSet(viewsets.ModelViewSet):
    """Returns All Beer Styles"""
    serializer_class = serializers.hop.SimpleHopSerializer
    queryset = Hop.objects.all()

class YeastTypeViewSet(viewsets.ModelViewSet):
    """Returns All Beer Styles"""
    serializer_class = serializers.yeast.YeastTypeSerializer
    queryset = YeastType.objects.all()

class YeastViewSet(viewsets.ModelViewSet):
    """Returns All Beer Styles"""
    serializer_class = serializers.yeast.SimpleYeastSerializer
    queryset = Yeast.objects.all()
