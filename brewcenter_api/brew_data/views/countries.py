from django.conf import settings
from rest_framework import viewsets, serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from brew_data import models, serializers
from accounts.auth import TokenAuthentication

import pycountry


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

        # get country codes from pycountry.  place the pieces we want into a dict
        country_codes = [{"id": ind + 1, "alpha_2" : country.alpha_2, "alpha_3": country.alpha_3} for ind, country in enumerate(list(pycountry.countries))]

        serializer = rf_serializers.ListSerializer(
            country_codes if request.auth is not None else country_codes[:settings.UNAUTHENTICATED_RESULTS_COUNT],
            child=serializers.CountryCodeSerializer()
        )

        return Response(serializer.data)
