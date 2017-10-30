from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from brew_data import models


class FermentableType(serializers.ModelSerializer):
    """Simple FermentableType Serializer"""
    class Meta:
        model = models.FermentableType
        fields = ('id', 'name', 'abbreviation')

class FermentableTypeSuggestion(serializers.Serializer):
    """Serializes Fermentable Type Suggestions"""
    new_type = FermentableType()
    old_type_id = serializers.IntegerField(required=False)

    def validate_old_type_id(self, old_type_id):

        # verify that if the old_type_id is not None, it has an object
        if old_type_id is not None:
            old_type = models.FermentableType.objects.get(id=old_type_id)
            if old_type is None:
                raise serializers.ValidationError("old_type_id is specified but does not correspond to a FermentableType.")

        return True

    def create(self, validated_data):
        """
        Create a new Fermentable Type Suggestion.
        """
        new_type_data = validated_data.pop('new_type')
        new_type = models.FermentableType.objects.create(**new_type_data)
        old_type_id = validated_data.pop('old_type_id')

        suggestion = models.Suggestion.objects.create(
            content_type=ContentType.objects.get(model='fermentabletype'),
            suggested_object_id=new_type.id,
            replaced_object_id=old_type_id)

        return suggestion

class FermentableInstance(serializers.ModelSerializer):
    """Serializes a single fermentable instance object"""
    class Meta:
        model = models.FermentableInstance
        fields = (
            'id',
            'year',
            'color',
            'color_units',
            'ppg',
            'ppg',
            'dry_yield_percent',
            'dry_yield_fine_grind_percent',
            'moisture_percent',
            'diastatic_power_lintner',
            'protein_percent',
            'soluble_protein_percent',
            'nitrogen_percent',
        )

class Fermentable(serializers.ModelSerializer):
    """A simple serializer for fermentables"""
    type = FermentableType()
    instances = serializers.ListSerializer(child=FermentableInstance())

    class Meta:
        model = models.Fermentable
        fields = (
            'id',
            'name',
            'type',
            'country',
            'instances',
            'notes'
        )
