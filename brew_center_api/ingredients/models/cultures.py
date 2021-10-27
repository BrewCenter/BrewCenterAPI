from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.deletion import SET_NULL
from ingredients.models.origin import Origin
from ingredients.models.manufacturer import Manufacturer

class CultureType(models.Model):
    """
    Describes the group of cultures we're talkinga bout. Ex. Ale yeasts, Lager yeasts, lacto cultures
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class CultureForm(models.Model):
    """
    Describes the physical form that this manufacturer. Ex. Liquid, dry
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class FlocculationLabel(models.Model):
    """
    Used like an enum to provide flocculation descriptors. Ex. Low, Very Low, Medium, High
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Culture(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(CultureType, on_delete=models.CASCADE)
    form = models.ForeignKey(CultureForm, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.SET_NULL)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    min_temp_f = models.FloatField(null=True, blank=True)
    max_temp_f = models.FloatField(null=True, blank=True)
    alcohol_tolerance_percent =  models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    flocculation = models.ForeignKey(FlocculationLabel, on_delete=SET_NULL, null=True, blank=True)
    min_attenuation_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    max_attenuation_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    notes = models.TextField(null=True, blank=True)
    best_for = models.CharField(max_length=255, null=True, blank=True)
    max_reuse = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    is_pof_positive = models.BooleanField(null=True, blank=True)
    is_glucoamylase_positive = models.BooleanField(null=True, blank=True)
    is_zymocide_no1 = models.BooleanField(null=True, blank=True)
    is_zymocide_no2 = models.BooleanField(null=True, blank=True)
    is_zymocide_no28 = models.BooleanField(null=True, blank=True)
    is_zymocide_klus = models.BooleanField(null=True, blank=True)
    is_zymocide_neutral = models.BooleanField(null=True, blank=True)
    

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

