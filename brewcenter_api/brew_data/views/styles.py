from rest_framework import serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers


class Styles(APIView):
    """
    Methods to Retrieve and Suggest Beer Styles.
    """
    authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        Returns all the beer styles. Do not show suggested
        beer styles by default.
        """
        serializer = rf_serializers.ListSerializer(models.Style.objects.all(), child=serializers.SimpleStyleSerializer())
        return Response(serializer.data)
