"""
Define the brew_data module URLs here and point them to their respective views.
"""
from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'styles', views.StyleViewSet)
router.register(r'countries', views.CountryViewSet)
router.register(r'ingredients/fermentables', views.FermentableViewSet)
router.register(r'ingredients/fermentable/types', views.FermentableTypeViewSet)
router.register(r'ingredients/hops', views.HopViewSet)
router.register(r'ingredients/hop/types', views.HopTypeViewSet)
router.register(r'ingredients/yeasts', views.YeastViewSet)
router.register(r'ingredients/yeast/types', views.YeastTypeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]

# urlpatterns = [
#     url(r'^styles$', views.styles, name='styles'),
#     url(r'^countries$', views.countries, name='countries'),
#     url(r'^ingredients/fermentables$', views.fermentables, name='fermentables'),
#     url(r'^ingredients/fermentable/types$', views.fermentable_types, name='fermentable_types'),
#     url(r'^ingredients/hops$', views.hops, name='fermentables'),
#     url(r'^ingredients/hop/types$', views.hop_types, name='hop_types'),
#     url(r'^ingredients/yeast$', views.yeast, name='yeast'),
#     url(r'^ingredients/yeast/types$', views.yeast_types, name='yeast_types'),
# ]