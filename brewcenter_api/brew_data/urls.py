"""
Define the brew_data module URLs here and point them to their respective views.
"""
from django.conf.urls import url
from brew_data import views

urlpatterns = [
	url(r'^styles$', views.Styles.as_view()),
    url(r'^countries$', views.Countries.as_view(), name='countries'),
    url(r'^ingredients/fermentables$', views.Fermentables.as_view(), name='fermentables'),
    url(r'^ingredients/fermentable/types$', views.FermentableTypes.as_view(), name='fermentable_types'),
    url(r'^ingredients/hops$', views.Hops.as_view(), name='hops'),
    url(r'^ingredients/hop/types$', views.HopTypes.as_view(), name='hop_types'),
    url(r'^ingredients/yeast$', views.Yeast.as_view(), name='yeast'),
    url(r'^ingredients/yeast/types$', views.YeastTypes.as_view(), name='yeast_types'),
]