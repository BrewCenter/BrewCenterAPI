from django.db import models
from brew_data.models import CountryCode


class FermentableType(models.Model):
    """
    Defines a fermentale type. Examples include:
    - Grain
    - Dry Malt Extract (DME)
    - Liquid Malt Extract (LME)
    """
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name


class Fermentable(models.Model):
    """
    Defines a fermentable object. A Fermentable is some object
    containing sugar that can be eated by yeast to product
    alcohol.
    """

    # Model Fields
    name = models.CharField(max_length=255)
    type = models.ForeignKey(FermentableType,
                             related_name="fermentables_with_type")
    country = models.ForeignKey(CountryCode,
                                related_name="fermentables_from_country",
                                null=True,
                                blank=True)
    ppg = models.FloatField(null=True, blank=True)
    lovibond = models.FloatField(null=True, blank=True)
    moisture = models.FloatField(null=True, blank=True)
    diastatic_power = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    # this is a percentage
    max_in_batch = models.FloatField(null=True, blank=True)
    is_mashed = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
