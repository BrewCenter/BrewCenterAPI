from rest_framework import serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers


class Countries(APIView):
    """
    View to retrieve all countries from the API
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        Returns all countries in the system.
        """
        serializer = rf_serializers.ListSerializer(models.CountryCode.objects.all(), child=serializers.CountryCodeSerializer())
        return Response(serializer.data)
