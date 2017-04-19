"""
Define the brew_data module URLs here and point them to their respective views.
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^styles$', views.styles, name='styles'),
    url(r'^countries$', views.countries, name='countries'),
    url(r'^ingredients/fermentables$', views.fermentables, name='fermentables'),
    url(r'^ingredients/fermentable/types$', views.fermentable_types, name='fermentable_types'),
    url(r'^ingredients/hops$', views.hops, name='fermentables'),
    url(r'^ingredients/hop/types$', views.hop_types, name='hop_types'),
    url(r'^ingredients/yeast$', views.yeast, name='yeast'),
    url(r'^ingredients/yeast/types$', views.yeast_types, name='yeast_types'),
]