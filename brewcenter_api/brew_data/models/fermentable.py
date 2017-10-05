from django.db import models
from brew_data.validators import country_code_validator


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
    type = models.ForeignKey(FermentableType, related_name="fermentables_with_type")
    country = models.CharField(max_length=3,null=True, blank=True,validators=[country_code_validator])
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

    def json(self):
        """return the fermentable object as JSON"""
        return "{{{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}}}".format(
                "name:" + self.name,
                "type:" + self.type.name,
                "country:" + self.country.code,
                "ppg:" + self.ppg,
                "lovibond:" + self.lovibond,
                "moisture:" + self.moisture,
                "diastatic_power:" + self.diastatic_power,
                "protein:" + self.protein,
                "max_in_batch:" + self.max_in_batch,
                "is_mashed:" + self.is_mashed,
                "notes:" + self.notes
            )
