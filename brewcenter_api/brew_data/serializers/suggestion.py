from rest_framework import serializers
from brew_data.models import Suggestion

class SimpleSuggestionSerializer(serializers.ModelSerializer):
    """A simple serializer for hops"""
    class Meta:
        model = Suggestion
        fields = (
            'id',
            'content_object',
            'submitted_by_user',
        )