from django.core.management import BaseCommand
from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework_swagger import renderers

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # httprequest = HttpRequest()
        # httprequest.user = FakeUser()
        # httprequest.META = {
        #     'SERVER_NAME': 'http://localhost/',
        #     'SERVER_PORT': '80'
        # }
        # request = Request(httprequest)
        # request.auth = True
        generator = SchemaGenerator()
        schema = generator.get_schema()
        json_data = renderers.OpenAPIRenderer().\
            render(schema, renderer_context={'response': Response(schema)}).decode('utf_8')
        with open('documentation.json', 'w') as docs:
            docs.write(json_data)
        print('Documentation written to documentation.json')
