"""
Define the brew_data module URLs here and point them to their respective views.
"""
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    url(r'^authenticate$', obtain_jwt_token, name='authenticate'),
]
