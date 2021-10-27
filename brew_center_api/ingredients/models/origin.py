from django.db import models

class Country(models.Model):
    """Defines a country and it's code(2 or 3 letter code, e.g. US)"""
    name = models.CharField(max_length=80)
    iso_code = models.CharField(max_length=3)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name = "Country"
        verbose_name_plural = "Countries"

class Origin(models.Model):
    """Defines an origin for an ingredient (I.e. Where the ingredient came from)"""
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
