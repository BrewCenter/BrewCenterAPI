import datetime

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
    is_active = models.BooleanField(default=False)

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
    type = models.ForeignKey(FermentableType)
    country = models.ForeignKey(CountryCode, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class FermentableInstance(models.Model):
    """
    A fermentable instance is a specific instance of a fermentable from a
    specific year. If a fermentable is not dependent on a year, the year
    value should be null, and there should only be one FermentableInstance
    for the Fermentable. E.g. For Sugars that don't change year-to-year.
    """

    YEAR_CHOICES = []
    for r in range(2000, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))

    fermentable = models.ForeignKey(Fermentable, related_name="instances")

    year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    color = models.FloatField(null=True, blank=True)
    color_units = models.TextField(choices=[('L','L'),('SRM','SRM')], max_length=3, null=True, blank=True)
    ppg = models.FloatField(null=True, blank=True)
    dry_yield_percent = models.FloatField(null=True, blank=True)
    dry_yield_fine_grind_percent = models.FloatField(null=True, blank=True)
    moisture_percent = models.FloatField(null=True, blank=True)
    diastatic_power_lintner = models.FloatField(null=True, blank=True)
    protein_percent = models.FloatField(null=True, blank=True)
    soluble_protein_percent = models.FloatField(null=True, blank=True)
    nitrogen_percent = models.FloatField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    notes=models.TextField(null=True, blank=True)
