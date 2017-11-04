from django.test import TestCase
from rest_framework.test import APIClient


class YeastTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_yeast_get(self):
        response = self.client.get('/data/ingredients/yeast')
        assert response.status_code == 200

    def test_yeast_types_get(self):
        response = self.client.get('/data/ingredients/yeast/types')
        assert response.status_code == 200

class HopTestCase(TestCase):
    """Test for Hops and HopTypes View"""
    def setUp(self):
        self.client = APIClient()
        
    def tearDown(self):
        del(self.client)
    
    def test_hops_get(self):
        response = self.client.get('/data/ingredients/hops')
        self.assertEqual(response.status_code, 200)
        
    def test_hop_types_get(self):
        response = self.client.get('/data/ingredients/hops/types')
        self.assertEqual(response.status_code, 200)
    
    