from django.db import models
from brew_data.models import CountryCode


class HopType(models.Model):
    """
    Defines a fermentale type. Examples include:
    - Aroma
    - Bittering
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Hop(models.Model):
    """
    Defines a fermentable object. A Fermentable is some object
    containing sugar that can be eated by yeast to product
    alcohol.
    """

    # Model Fields
    name = models.CharField(max_length=255)
    type = models.ForeignKey(HopType, related_name="hops_with_type")
    country = models.ForeignKey(CountryCode, related_name="hops_from_country",
                                null=True, blank=True)
    alpha_acids = models.FloatField(null=True, blank=True)
    beta_acids = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
