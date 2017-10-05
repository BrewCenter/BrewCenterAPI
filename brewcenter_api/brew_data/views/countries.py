import itertools

from iso3166 import countries_by_alpha3, countries_by_alpha2
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


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
        all_countries = [{'code': i} for i in itertools.chain(countries_by_alpha3,countries_by_alpha2)]
        return Response(all_countries)
