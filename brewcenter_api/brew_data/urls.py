"""
Define the brew_data module URLs here and point them to their respective views.
"""
from brew_data import views

from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'all', views.All, 'all')
router.register(r'styles', views.Styles, 'styles')
router.register(r'countries', views.Countries, 'countries')
router.register(r'ingredients/fermentables/types', views.FermentableTypes, 'fermentable_types')
router.register(r'ingredients/fermentables/types/{pk}', views.FermentableTypes, 'fermentable_types')
router.register(r'ingredients/fermentables/instances', views.FermentableInstances, 'fermentable_instances')
router.register(r'ingredients/fermentables',views.Fermentables, 'fermentables')
router.register(r'ingredients/hops', views.Hops, 'hops')
router.register(r'ingredients/hops/types', views.HopTypes, 'hop_types')
router.register(r'ingredients/yeast', views.Yeast, 'yeast')
router.register(r'ingredients/yeast/types', views.YeastTypes, 'yeast_types')

urlpatterns = router.urls
