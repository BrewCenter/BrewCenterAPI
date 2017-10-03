from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers
# Create your views here.
class SwaggerSchemaView(APIView):
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema()
        return Response(schema)
