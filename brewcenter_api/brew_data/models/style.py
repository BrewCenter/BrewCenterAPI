from django.db import models

class Style(models.Model):
    """
    Defines a beer style type. Examples include:
    - Ale
    - Lager
    """
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    og_min = models.FloatField(null=True, blank=True)
    og_max = models.FloatField(null=True, blank=True)
    fg_min = models.FloatField(null=True, blank=True)
    fg_max = models.FloatField(null=True, blank=True)
    ibu_min = models.FloatField(null=True, blank=True)
    ibu_max = models.FloatField(null=True, blank=True)
    srm_min = models.FloatField(null=True, blank=True)
    srm_max = models.FloatField(null=True, blank=True)
    abv_min = models.FloatField(null=True, blank=True)
    abv_max = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name
