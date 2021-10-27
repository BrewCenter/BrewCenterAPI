from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from ingredients.models.origin import Origin
from ingredients.models.manufacturer import Manufacturer 

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

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class GrainType(models.Model):
    """
    Defines grain types. Examples include:
    - Base
    - Caramel
    - Flaked
    """
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class FermentableBase(models.Model):
    """
    Defines the basic properties used by all fermentables.
    
    Attributes:
        name                    The name of the fermentable.
        type                    A foreign key reference to a FermentableType (e.g. "Grain")
        is_active               True if this instance should be used and queryable
        origin                  A foreign key reference to a Origin model (where this fermentable comes from)
        manufacturer            The company that produces this fermentable product
        product_id              A freeform identifying code which should correspond to how the manufacturer identifies this product.
        potential_ppg           The potential specific gravity points per pound (ppg) of the fermentable disolved in a gallon of water.
        color_srm               The color contributed by the fermentable, measured using the Standard Reference Method (SRM). Ranges from 0 (clear) to 60 (black)
        fermentability_percent  Used in Extracts to indicate a baseline typical apparent attenuation for a typical medium attenuation yeast.
        notes                   Any remarks on the flavor or other qualities contributed by this fermentable.
    """
    name = models.CharField(max_length=255)
    type = models.ForeignKey(FermentableType, on_delete=models.RESTRICT)
    is_active = models.BooleanField(default=False)
    origin = models.ForeignKey(Origin, null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True, on_delete=models.SET_NULL)
    product_id = models.CharField(max_length=255, null=True, blank=True)
    potential_ppg = models.FloatField(validators=[MinValueValidator(0)])
    color_srm = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    notes = models.TextField(null=True, blank=True)
    fermentability_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Grain(models.Model):
    """
    An extension of the FermentableBase model which includes data specific to grains as fermentables.

    Attributes:
        fermentable                 A one-to-one foreign key referencing the FermentableBase model which holds the attributes shared by all fermentables.
        moisture_percent            The percentage of this grain that holds moisture. Values range from 0 to 1.
        alpha_amylase               Where diastatic power gives the total amount of all enzymes, alpha amylase, also known as dextrinizing units, refers to only the total amount of alpa amylase in the malted grain. A value of 25-50 is desirable for base malt.
        diastatic_power_lintner     Diastatic power is a measurement of malted grains enzymatic content. A value of 35 Lintner is needed to seslf-convert, while a value of 100 or more is desirable.
        protein_percent             The percentage of protein found in the grain. Higher values may indicate haze.
        kolbach_index_percent       The Kolbach Index of the grain measured as a percentage.
        max_in_batch_percent        The recommended maximum amount of this grain to be used in a grain bill, as a percentage of the total grain bill.
        recommend_mash              True if it is recommended to mash this grain.
        glassy_percent              Used to indicate the ‘crystallized’ percentage of starches for crystal malts.
        half_percent
        plump_percent               The percentage of grain that masses through sieves with gaps of 7/64 and 6/64, desired values of 80% or higher which indicate plump kernels.
        mealy_percent               The opposite of glassy, a mealy kernel is one that is not glassy. Base malt should be at least 90%, single step mashes generally require 95% or higher.
        thru_percent                The Percentage of grain that makes it through a thin mesh screen, typically 5/64 inch. Values less than 3% are desired.

        friability_percent          Friability is the measure of a malts ability to crumble during the crush, and is used as an indicator for easy gelatinization of the grain and starches, as well as modification of the malt. Value of 85% of higher indicates a well modified malt and is suitable for single step mashes. Lower values may require a step mash.
        di_ph	 	                The pH of the resultant wort for 1 lb of grain mashed in 1 gallon of distilled water. Used in many water chemistry / mash pH prediction software.
        viscosity_cp	 	        The measure of wort viscosity, typically associated with the breakdown of beta-glucans. The higher the viscosity, the greater the need for a glucan rest and the less suitable for a fly sparge. Measured in centipoise.
        dms_precursors_ppm	 	    The amount of DMS precursors, namely S-methyl methionine (SMM) and dimethyl sulfoxide (DMSO) in the malt which convert to dimethyl sulfide (DMS). Measured in parts per million.
        fan_ppm	 	                Free Amino Nitrogen (FAN) is a critical yeast nutrient. Typical values for base malt is 170.
        beta_glucan_ppm	 	        Values of 180 or more may suggest a glucan rest and avoiding fly sparging.

        fine_grind_potential_ppg    Percentage yield compared to succrose of a fine grind. eg 80%
        coarse_grind_potential_ppg  Percentage yield compared to succrose of a fine grind. eg 60%

    """
    type = models.ForeignKey(GrainType, on_delete=models.RESTRICT, related_name="grains")
    fermentable = models.OneToOneField(FermentableBase, on_delete=models.CASCADE, related_name="grain")
    moisture_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    alpha_amylase = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    diastatic_power_lintner = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    protein_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    kolbach_index_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    max_in_batch_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    recommend_mash = models.BooleanField(default=True)
    glassy_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    plump_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    mealy_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    thru_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    friability_percent = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(1)])
    di_ph = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(14)])
    viscosity_cp = models.FloatField(null=True, blank=True)
    dms_precursors_ppm = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    fan_ppm = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    beta_glucan_ppm = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    fine_grind_potential_ppg = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])
    coarse_grind_potential_ppg = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0)])

    class Meta:
        order_with_respect_to = 'fermentable'

    def __str__(self):
        return self.fermentable.__str__()