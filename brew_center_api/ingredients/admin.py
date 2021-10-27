from typing import Counter
from django.contrib import admin
from ingredients.models import *

admin.site.register(Country)
admin.site.register(Origin)
admin.site.register(Manufacturer)
admin.site.register(FermentableType)
admin.site.register(GrainType)
admin.site.register(FermentableBase)
admin.site.register(Grain)
