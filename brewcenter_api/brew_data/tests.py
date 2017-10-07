from django.test import TestCase

from brew_data.models import CountryCode
from brew_data.models import FermentableType, Fermentable

class TestFactory():
    """Creates models and structures for testing"""

    def create_country_code():
        CountryCode.objects.create(code="T1")

    def create_fermentable_type():
        FermentableType.objects.create(name="Test Grain", abbreviation="TG")

    def create_fermentable():
        TestFactory.create_country_code()
        TestFactory.create_fermentable_type()
        country_code_id = CountryCode.objects.get(code="T1").id
        fermentable_type_id = FermentableType.objects.get(name="Test Grain").id
        Fermentable.objects.create(
            name="Test Fermentable",
            type_id=fermentable_type_id,
            country_id=country_code_id,
            ppg=38.4,
            lovibond=20.4,
            moisture=4.7,
            protein=10.8,
            max_in_batch=50,
            is_mashed=True,
            notes="This is a test note field"
        )
        

class CountryCodeTestCase(TestCase):
    """Tests basic aspects of creating a country code"""

    def test_create_code(self):
        """Tests that you can create a basic country code"""
        TestFactory.create_country_code()
        self.assertIsNotNone(CountryCode.objects.get(code="T1"))


class FermentableTestCase(TestCase):
    """Tests the Fermentable Model"""
    
    def test_create_fermentable_type(self):
        """Tests that a fermentable type can be created and queried"""
        TestFactory.create_fermentable_type()
        self.assertIsNotNone(FermentableType.objects.get(name="Test Grain"))

    def test_create_fermentable(self):
        """Tests basic fermentable creation"""
        TestFactory.create_fermentable()
        self.assertIsNotNone(Fermentable.objects.get(name="Test Fermentable"))

