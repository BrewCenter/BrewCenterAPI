from django.db import models

class Manufacturer(models.Model):
    """Defines a producer or manufacturer of ingredients"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
