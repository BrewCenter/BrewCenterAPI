"""
Define the brew_data module URLs here and point them to their respective views.
"""
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from accounts import views

urlpatterns = [
    url(r'^tokens$', views.Tokens.as_view()),
    url(r'^tokens/(?P<token>[a-zA-Z0-9]+)$', views.Tokens.as_view()),
]
