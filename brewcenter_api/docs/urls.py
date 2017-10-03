from django.conf.urls import url
from docs.views import SwaggerSchemaView

urlpatterns = [
    url(r'/', SwaggerSchemaView.as_view())
]