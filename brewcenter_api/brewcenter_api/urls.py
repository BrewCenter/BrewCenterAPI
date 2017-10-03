"""brewcenter_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import refresh_jwt_token

schema_view = get_swagger_view(title='BrewCenter API')

urlpatterns = [
    url(r'^data/', include('brew_data.urls', namespace='data')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^documentation', schema_view)
    url(r'^auth/token-refresh', refresh_jwt_token),
]
