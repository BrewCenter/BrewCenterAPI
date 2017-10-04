from django.conf import settings
from rest_framework import viewsets, serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers


class Countries(viewsets.ViewSet):
    """
    View to retrieve all countries from the API
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        """
        Returns all countries in the system.
        """
        serializer = rf_serializers.ListSerializer(
            models.CountryCode.objects.all() if request.auth is not None else models.CountryCode.objects.all()[:settings.UNAUTHENTICATED_RESULTS_COUNT],
            child=serializers.CountryCodeSerializer()
        )
        return Response(serializer.data)
