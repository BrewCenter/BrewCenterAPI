from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from brew_data.models import Suggestion


class YeastType(models.Model):
    """
    Defines a Yeast type. Examples include:
    - Ale
    - Lager
    """
    name = models.CharField(max_length=255)
    suggestion = GenericRelation(Suggestion)

    def __str__(self):
        return self.name


class Yeast(models.Model):
    """
    Defines a fermentable object. A Fermentable is some object
    containing sugar that can be eated by yeast to product
    alcohol.
    """

    # Model Fields
    name = models.CharField(max_length=255)
    type = models.ForeignKey(YeastType, related_name="yeast_with_type")
    is_liquid = models.NullBooleanField(null=True, blank=True)
    lab = models.CharField(max_length=255)
    min_temp = models.FloatField(null=True, blank=True)
    max_temp = models.FloatField(null=True, blank=True)
    flocculation = models.CharField(max_length=255, null=True, blank=True)
    attenuation = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    suggestion = GenericRelation(Suggestion)

    def __str__(self):
        return self.name
