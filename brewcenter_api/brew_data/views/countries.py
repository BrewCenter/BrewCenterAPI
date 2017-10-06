from rest_framework import viewsets, serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers
from accounts.auth import TokenAuthentication


class Countries(viewsets.ViewSet):
    """
    View to retrieve all countries from the API
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        """
        Returns all countries in the system.
        """
        serializer = rf_serializers.ListSerializer(
            models.CountryCode.objects.all(),
            child=serializers.CountryCodeSerializer())

        return Response(serializer.data)
