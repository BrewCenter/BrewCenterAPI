from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ingredients.models.origin import Origin
from ingredients.models.manufacturer import Manufacturer

class HopForm(models.Model):
    """
    Defines a form that hops can take. Ex: Pellets, leaf
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class HopUse(models.Model):
    """
    The way the hop is used. Ex: Aroma, bittering
    """
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class HopVariety(models.Model):
    name = models.CharField(max_length=100)
    uses = models.ManyToManyField(HopUse, related_name="varieties")
    substitutes = models.ManyToManyField('self', blank=True, symmetrical=True)
    notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class HopProduct(models.Model):
    variety = models.ForeignKey(HopVariety, related_name="products", on_delete=models.CASCADE)
    form = models.ForeignKey(HopForm, related_name="products", on_delete=models.CASCADE)
    origin = models.ForeignKey(Origin, null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.SET_NULL)
    product_id = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2050)])
    alpha_acid_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    beta_acid_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    is_active = models.BooleanField(default=False)
    percent_lost_after_6_months = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])

    # These are really specific oil content percentages
    total_oil_ml_per_100g = models.FloatField(null=True, blank=True)
    humulene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    caryophyllene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    myrcene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    farnesene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    geraniol_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    b_pinene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    linalool_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    limonene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    nerol_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    pinene_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    polyphenols_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    xanthohumol_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])


    class Meta:
        order_with_respect_to = 'variety'
        verbose_name = 'Hop'
        verbose_name_plural = 'Hops'

    def __str__(self):
        display_name = self.variety.name
        if self.manufacturer:
            display_name += '({0})'.format(str(self.manufacturer))
        return display_name
