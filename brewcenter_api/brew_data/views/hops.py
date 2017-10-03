from rest_framework import viewsets, serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers
from accounts.auth import TokenAuthentication

class HopTypes(viewsets.ViewSet):
    """
    View to Retrieve hop Types.
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        """
        Returns all hop types in the system
        """
        serializer = rf_serializers.ListSerializer(models.HopType.objects.all(), child=serializers.HopTypeSerializer())
        return Response(serializer.data)

class Hops(viewsets.ViewSet):
    """
    View to Retrieve all approved hops and Suggest new hops.
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        """
        Returns all hops that are approved in the system by default.
        """
        serializer = rf_serializers.ListSerializer(models.Hop.objects.all(), child=serializers.SimpleHopSerializer())
        return Response(serializer.data)
