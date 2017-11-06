from django.conf import settings
from rest_framework import viewsets, serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers
from accounts.auth import TokenAuthentication


class Styles(viewsets.ViewSet):
    """Methods to Retrieve and Suggest Beer Styles."""

    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        """Return all the beer styles. Do not show suggested beer styles by default."""
        styles = models.Style.objects.all()
        if request.auth is None:
            styles = styles[:settings.UNAUTHENTICATED_RESULTS_COUNT]

        serializer = rf_serializers.ListSerializer(
            styles,
            child=serializers.SimpleStyleSerializer()
        )
        return Response(serializer.data)
