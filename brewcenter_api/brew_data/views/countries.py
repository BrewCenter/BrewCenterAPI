import itertools

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from iso3166 import countries_by_alpha2,countries_by_alpha3
from rest_framework_jwt.authentication import JSONWebTokenAuthentication




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
        all_countries = [{'code': i} for i in itertools.chain(countries_by_alpha3,countries_by_alpha2)]
        return Response(all_countries)
