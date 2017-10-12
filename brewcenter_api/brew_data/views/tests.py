from django.test import TestCase
from django.urls import reverse
from brew_data.views import Yeast, YeastTypes
from rest_framework.test import APIRequestFactory, APIClient, RequestsClient, force_authenticate
from rest_framework.authtoken.models import Token


class YeastTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_yeast_get(self):
        response = self.client.get('/data/ingredients/yeast')
        assert response.status_code == 200

    def test_yeast_types_get(self):
        response = self.client.get('/data/ingredients/yeast/types')
        assert response.status_code == 200
