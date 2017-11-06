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

        return old_type_id

    def create(self, validated_data):
        """Create a new Fermentable Type Suggestion."""
        new_type_data = validated_data.pop('new_type')
        new_type = models.FermentableType.objects.create(**new_type_data)

        old_type_id = None
        if 'old_type_id' in validated_data:
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


class FermentableInstanceSuggestion(serializers.Serializer):
    """Serializes Suggestions for Fermentable Instances."""

    new_instance = FermentableInstance()
    old_instance_id = serializers.IntegerField(required=False, allow_null=True)
    fermentable_id = serializers.IntegerField()

    def validate_old_instance_id(self, old_instance_id):
        """Validate that the old_instance_id is correct if set."""
        # verify that if the old_type_id is not None, it has an object
        if old_instance_id is not None:
            old_instance = models.FermentableInstance.objects.get(id=old_instance_id)
            if old_instance is None:
                raise serializers.ValidationError("old_instance is specified but does not correspond to a FermentableInstance.")

        return old_instance_id

    def validate_fermentable_id(self, fermentable_id):
        """Make sure this is a real fermentable id."""
        fermentable = models.Fermentable.objects.get(id=fermentable_id)
        if fermentable is None:
            raise serializers.ValidationError("fermentable_id does not belong to a Fermentable.")
        return fermentable_id

    def create(self, validated_data):
        """Save the Fermentable Instance Suggestion."""
        fermentable_id = validated_data.pop('fermentable_id')
        new_instance_data = validated_data.pop('new_instance')
        new_instance = models.FermentableInstance.objects.create(**new_instance_data)
        new_instance.fermentable_id = fermentable_id
        new_instance.save()

        old_instance_id = None
        if 'old_instance_id' in validated_data:
            old_instance_id = validated_data.pop('old_instance_id')

        suggestion = models.Suggestion.objects.create(
            content_type=ContentType.objects.get(model='fermentableinstance'),
            suggested_object_id=new_instance.id,
            replaced_object_id=old_instance_id)

        return suggestion


class Fermentable(serializers.ModelSerializer):
    """A simple serializer for fermentables."""

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


class SimpleFermentable(serializers.ModelSerializer):
    """A simple serializer for fermentables."""

    type_id = serializers.IntegerField()
    instances = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Fermentable
        fields = (
            'id',
            'name',
            'type_id',
            'country',
            'instances',
            'notes'
        )


class FermentableSuggestion(serializers.Serializer):
    """Serializes Suggestions for Fermentables."""

    new_fermentable = SimpleFermentable()
    old_fermentable_id = serializers.IntegerField(required=False)

    def validate_old_fermentable_id(self, old_fermentable_id):
        """Validate that the old_fermentable_id is correct if set."""
        # verify that if the old_type_id is not None, it has an object
        if old_fermentable_id is not None:
            old_fermentable_id = models.Fermentable.objects.get(id=old_fermentable_id)
            if old_fermentable_id is None:
                raise serializers.ValidationError("old_fermentable_id is specified but does not correspond to a Fermentable.")

        return old_fermentable_id

    def validate(self, data):
        """
        Verify that only existing intances connected to the old fermentable id are present here.
        The instances part of this data should only be used for removing certain fermentable
        instances from the data.
        """
        if 'instances' in data['new_fermentable']:
            for instance_id in data['new_fermentable']['intances']:

                instance = models.FermentableInstance.objects.get(pk=instance_id)
                if instance is None:
                    raise serializers.ValidationError(str(instance_id) + " does not correspond to a FermentableInstance.")

                if instance is not None:
                    if instance.fermentable.id != old_fermentable_id:
                        raise serializers.ValidationError(
                            "Instance with id '{0}' does not belong to the old fermentable with "
                            "id '{1}'. New instances cannot be added with this endpoint. This "
                            "should only be used for taking old instances out of the suggestion."
                            .format(intance_id, data['old_fermentable_id']))
        return super(FermentableSuggestion, self).validate(data)

    def create(self, validated_data):
        """Save the Fermentable Instance Suggestion."""
        old_fermentable_id = validated_data.pop('old_fermentable_id')
        new_fermentable_data = validated_data.pop('new_fermentable')

        new_fermentable_instances = []
        if 'instances' in new_fermentable_data:
            new_fermentable_instances = new_fermentable_data.pop('instances')

        new_fermentable = models.Fermentable.objects.create(**new_fermentable_data)

        # for each instance id copy the instance if it is already attached to a fermentable and attach it
        # to this instead.
        # TODO: Fix this so it's not wasting data copying stuff. A proper implementation would introduce
        # a new table for the relationship. But I'm going lean and fast! Ya! Agile! Woot! WORK IT
        for instance_id in new_fermentable_instances:
            instance = models.FermentableInstance.objects.get(id=instance_id)

            # if the instance doesn't have a fermentable throw an error
            # this method should only be used for modifying existing instances on a fermentable
            if instance.fermentable is None:
                raise ser

            # otherwise copy the instance
            else:
                instance.pk = instance.id = None
                instance.fermentable = new_fermentable

            instance.save()

        suggestion = models.Suggestion.objects.create(
            content_type=ContentType.objects.get(model='fermentable'),
            suggested_object_id=new_fermentable.id,
            replaced_object_id=old_fermentable_id)

        return suggestion
