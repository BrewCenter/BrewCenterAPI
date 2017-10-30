from django.conf import settings
from rest_framework import viewsets, serializers as rf_serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import permission_classes
from django.shortcuts import get_object_or_404

from brew_data import models, serializers
from accounts.auth import TokenAuthentication

from django.contrib.contenttypes.models import ContentType

class FermentableTypes(viewsets.ViewSet):
    """
    View to Retrieve Fermentable ingredient Types.
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)

    def get_permissions(self):
        """Define custom permissions for different methods"""

        # at minimum require users to be authenticated
        self.permission_classes = [IsAuthenticated]
        # for PUT requests require users to be admins
        if self.request.method == 'PUT':
            self.permission_classes.append(IsAdminUser)

        return super(viewsets.ViewSet, self).get_permissions()

    def list(self, request):
        """
        Returns all fermentable types in the system
        """
        fermentable_types = fermentable_types = models.FermentableType.objects.filter(is_active=True)
        # if the user is authenticated return all valid fermentable types
        if request.auth is None:
            fermentable_types = fermentable_types[:settings.UNAUTHENTICATED_RESULTS_COUNT]

        serializer = rf_serializers.ListSerializer(
            fermentable_types,
            child=serializers.FermentableType()
        )
        return Response(serializer.data)

    def update(self, request, pk=None):
        """Allows admins to edit fermentable types directly."""
        fermentable_type = get_object_or_404(models.FermentableType, pk=pk)

        serializer = serializers.FermentableType(data=request.data)
        if serializer.is_valid():
            fermentable_type = serializer.save()

            # if the fermentable was marked as is_active then set that flag
            if request.data['is_active'] is not None:
                fermentable_type.is_active = request.data['is_active']
                fermentable_type.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def create(self, request):
        """
        Suggests a brand new fermentable type.
        """
        serializer = serializers.FermentableTypeSuggestion(data=request.data)

        if serializer.is_valid():
            suggestion = serializer.save()
            suggestion = models.Suggestion.objects.get(id=suggestion.id)

            new_type = models.FermentableType.objects.get(id=suggestion.suggested_object_id)
            new_type_data = serializers.FermentableType(new_type).data

            data = {
                "old_type_id": suggestion.replaced_object_id,
                "new_type": new_type_data
            }
            return Response(data)
        else:
            return Response(serializer.errors)

class Fermentables(viewsets.ViewSet):
    """
    View to Retrieve all approved fermentables and Suggest new
    fermentables.
    """
    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )

    def list(self, request):
        """
        Returns all fermentables that are approved in the system by default.
        """
        serializer = rf_serializers.ListSerializer(
            models.Fermentable.objects.all() if request.auth is not None else models.Fermentable.objects.all()[:settings.UNAUTHENTICATED_RESULTS_COUNT],
            child=serializers.Fermentable()
        )
        return Response(serializer.data)