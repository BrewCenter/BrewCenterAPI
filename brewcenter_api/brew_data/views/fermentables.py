from rest_framework import serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers


class FermentableTypes(APIView):
    """
    View to Retrieve Fermentable ingredient Types.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        Returns all fermentable types in the system
        """
        serializer = rf_serializers.ListSerializer(models.FermentableType.objects.all(), child=serializers.FermentableTypeSerializer())
        return Response(serializer.data)

class Fermentables(APIView):
    """
    View to Retrieve all approved fermentables and Suggest new
    fermentables.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        Returns all fermentables that are approved in the system by default.
        """
        serializer = rf_serializers.ListSerializer(models.Fermentable.objects.all(), child=serializers.SimpleFermentableSerializer())
        return Response(serializer.data)
