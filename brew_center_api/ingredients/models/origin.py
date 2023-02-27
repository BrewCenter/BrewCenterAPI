from django.db import models

class Origin(models.Model):
    """Defines an origin for an ingredient (I.e. Where the ingredient came from)"""
    country_code = models.CharField(max_length=3)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
