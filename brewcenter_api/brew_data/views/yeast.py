from rest_framework import serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers

class YeastTypes(APIView):
    """
    Methods to Retrieve and Suggest new Yeast Types.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        Returns all approved yeast types by default.
        """
        serializer = rf_serializers.ListSerializer(models.YeastType.objects.all(), child=serializers.YeastTypeSerializer())
        return Response(serializer.data)

class Yeast(APIView):
    """
    Methods to Retrieve and Suggest new Yeast strains.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        Returns all approved yeast strains.
        """
        serializer = rf_serializers.ListSerializer(models.Yeast.objects.all(), child=serializers.SimpleYeastSerializer())
        return Response(serializer.data)
