from typing import Counter
from django.contrib import admin
from ingredients.models import *

admin.site.register(Country)
admin.site.register(Origin)
admin.site.register(Manufacturer)
admin.site.register(FermentableType)
admin.site.register(GrainType)
admin.site.register(Grain)
admin.site.register(FermentableBase)
admin.site.register(HopForm)
admin.site.register(HopUse)
admin.site.register(HopVariety)
admin.site.register(HopProduct)
admin.site.register(CultureType)
admin.site.register(CultureForm)
admin.site.register(FlocculationLabel)
admin.site.register(Culture)
