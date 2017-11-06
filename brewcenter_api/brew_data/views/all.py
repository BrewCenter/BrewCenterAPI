from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from accounts.auth import TokenAuthentication

from brew_data.views.countries import Countries
from brew_data.views.fermentables import Fermentables, FermentableTypes
from brew_data.views.hops import Hops, HopTypes
from brew_data.views.styles import Styles
from brew_data.views.yeast import Yeast, YeastTypes


class All(viewsets.ViewSet):
    """Methods to Retrieve all Brewcenter Data."""

    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        resources = {'countries': Countries,
                     'fermentables': Fermentables,
                     'fermentable_types': FermentableTypes,
                     'hops': Hops,
                     'hop_types': HopTypes,
                     'styles': Styles,
                     'yeast': Yeast,
                     'yeast_types': YeastTypes}

        response_data = {}
        for key, resource in resources.items():
            response_data[key] = resource.as_view({'get': 'list'})(request).data

        return Response(response_data)
