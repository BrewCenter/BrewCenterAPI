from django.test import TestCase

from brew_data.models import CountryCode
from brew_data.models import FermentableType, Fermentable
from brew_data.models import Hop, HopType


class TestFactory():
    """Creates models and structures for testing"""

    def create_country_code():
        country = CountryCode.objects.create(code="T1")
        return country

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

    def create_hop_type(name):
        """Create HopType object for testing"""
        type = HopType.objects.create(
            name=name
        )

        return type

    def create_hop(name, type, country, alpha_acids, beta_acids, notes):
        """Create Hop Object for Testing"""
        hop = Hop.objects.create(
            name=name,
            type=type,
            country=country,
            alpha_acids=alpha_acids,
            beta_acids=beta_acids,
            notes=notes
        )

        return hop


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


class HopTestCase(TestCase):
    """Test the Hop and HopType Models"""

    def setUp(self):
        """create instance-level variables for tests"""

        # Create HopType
        self.hoptype = TestFactory.create_hop_type('Test Hop Type')
        self.assertIsNotNone(self.hoptype)
        self.assertEqual(self.hoptype.name, 'Test Hop Type')

        # Create CountryCode
        self.country = TestFactory.create_country_code()
        self.assertIsNotNone(self.country)

        # Create Hop
        self.hop = TestFactory.create_hop(
            'Test Hop Name',
            self.hoptype,
            self.country,
            1.11,
            1.10,
            'These are test notes'
        )
        self.assertIsNotNone(self.hop)
        self.assertEqual(self.hop.type, self.hoptype)

    def test_create_hop_type(self):
        """TestFactory.create_hop_type should create new hop type object"""
        new_type = HopType.objects.get(name='Test Hop Type')

        self.assertEqual(self.hoptype, new_type)

    def test_hop_type_str_method(self):
        """Calling str(HopType) should return types name attribute"""
        self.assertEqual(self.hoptype.name, str(self.hoptype))

    def test_create_hop(self):
        """TestFactory.create_hop should create new hop object"""
        new_hop = Hop.objects.get(name='Test Hop Name')
        self.assertEqual(self.hop, new_hop)
