from django.test import TestCase

from brew_data.models import CountryCode
from brew_data.models import FermentableType, Fermentable


class TestFactory():
    """Creates models and structures for testing"""

    def create_country_code():
        CountryCode.objects.create(code="T1")

    def create_fermentable_type():
        new_ferm_type = FermentableType.objects.create(name="Test Grain",
                                                       abbreviation="TG")
        return new_ferm_type

    def create_fermentable():
        TestFactory.create_country_code()
        TestFactory.create_fermentable_type()
        country_code_id = CountryCode.objects.get(code="T1").id
        fermentable_type_id = FermentableType.objects.get(name="Test Grain").id
        new_fermentable = Fermentable.objects.create(
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

        return new_fermentable


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

    def test_fermentable_type_str_method(self):
        """Tests str(FermentableType) returns expected value"""
        test_fermentable_type = TestFactory.create_fermentable_type()
        self.assertEqual(
            str(test_fermentable_type),
            test_fermentable_type.name
        )

    def test_fermentable_str_method(self):
        """Tests str(Fermentable) returns expected value"""
        test_fermentable = TestFactory.create_fermentable()
        self.assertEqual(
            str(test_fermentable),
            test_fermentable.name
        )

    def test_fermentable_json_method(self):
        """
        Tests Fermentable.json method to ensure it returns the
        expected value
        """
        test_fermentable = TestFactory.create_fermentable()
        self.assertEqual(test_fermentable.name, "Test Fermentable")

        test_json = test_fermentable.json()
        print(test_json)

        self.assertEqual(expected_json, test_json)
