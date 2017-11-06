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
    """View to Retrieve Fermentable ingredient Types."""

    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)

    # def get_permissions(self):
    #     """Define custom permissions for different methods"""

    #     # at minimum require users to be authenticated
    #     self.permission_classes = [IsAuthenticated]
    #     # for PUT requests require users to be admins
    #     if self.request.method == 'PUT':
    #         self.permission_classes.append(IsAdminUser)

    #     return super(viewsets.ViewSet, self).get_permissions()

    def list(self, request):
        """Return all fermentable types in the system."""
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
        """Allow admins to edit fermentable types directly."""
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
        """Suggest a brand new fermentable type."""
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


class FermentableInstances(viewsets.ViewSet):
    """View to retrieve/update fermentable instances."""

    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)

    def get_permissions(self):
        """Define custom permissions for different methods."""
        # at minimum require users to be authenticated
        self.permission_classes = [IsAuthenticated]
        # for PUT requests require users to be admins
        if self.request.method == 'PUT':
            self.permission_classes.append(IsAdminUser)

        return super(viewsets.ViewSet, self).get_permissions()

    def create(self, request):
        """Create a new suggestion for a fermentable instance."""
        serializer = serializers.FermentableInstanceSuggestion(data=request.data)

        if serializer.is_valid():
            suggestion = serializer.save()
            suggestion = models.Suggestion.objects.get(id=suggestion.id)

            new_instance = models.FermentableInstance.objects.get(id=suggestion.suggested_object_id)
            new_instance_data = serializers.FermentableInstance(new_instance).data

            data = {
                "fermentable_id": new_instance.fermentable_id,
                "old_instance_id": suggestion.replaced_object_id,
                "new_instance": new_instance_data
            }

            return Response(data)
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        """Allow admins to update specific fermentable instance objects."""
        instance = get_object_or_404(models.FermentableInstance, pk=pk)

        serializer = serializers.FermentableInstance(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            if request.data['is_active'] is not None:
                instance.is_active = request.data['is_active']
                instance.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Fermentables(viewsets.ViewSet):
    """View to Retrieve all approved fermentables and Suggest new fermentables."""

    authentication_classes = (JSONWebTokenAuthentication, TokenAuthentication)

    def get_permissions(self):
        """Define custom permissions for different methods."""
        # at minimum require users to be authenticated
        self.permission_classes = [IsAuthenticated]
        # for PUT requests require users to be admins
        if self.request.method == 'PUT':
            self.permission_classes.append(IsAdminUser)

        return super(viewsets.ViewSet, self).get_permissions()

    def list(self, request):
        """Return all fermentables that are approved in the system by default."""
        fermentables = models.Fermentable.objects.filter(is_active=True)

        if request.auth is None:
            fermentables = fermentables[:settings.UNAUTHENTICATED_RESULTS_COUNT]

        serializer = rf_serializers.ListSerializer(
            fermentables,
            child=serializers.Fermentable()
        )
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new suggestion for a fermentable.
        """
        serializer = serializers.FermentableSuggestion(data=request.data)

        if serializer.is_valid():
            suggestion = serializer.save()
            suggestion = models.Suggestion.objects.get(id=suggestion.id)

            new_fermentable = models.Fermentable.objects.get(id=suggestion.suggested_object_id)
            new_fermentable_data = serializers.Fermentable(new_fermentable).data

            data = {
                "old_fermentable_id": suggestion.replaced_object_id,
                "new_fermentable": new_fermentable_data
            }

            return Response(data)

        else:
            return Response(serializer.errors)

    def update(self, request, pk=None):
        """Allow admins to update specific fermentable objects."""
        fermentable = get_object_or_404(models.Fermentable, pk=pk)

        serializer = serializers.SimpleFermentable(data=request.data)

        if serializer.is_valid():
            fermentable = serializer.save()

            if request.data['is_active'] is not None:
                fermentable.is_active = request.data['is_active']
                fermentable.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
