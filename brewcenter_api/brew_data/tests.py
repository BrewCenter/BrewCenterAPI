from django.test import TestCase

from brew_data.models import CountryCode
from brew_data.models import FermentableType, Fermentable, FermentableInstance
from brew_data.models import Hop, HopType


class TestFactory():
    """Creates models and structures for testing"""

    def create_country_code():
        country = CountryCode.objects.create(code="T1")
        return country

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
            notes="This is a test.")
        
        instance = FermentableInstance.objects.create(
            fermentable=new_fermentable,
            ppg=38.4,
            color=20.4,
            color_units='L',
            moisture_percent=4.7,
            protein_percent=10.8,
            notes="This is a test",
            is_active=True)

        return new_fermentable

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


class FermenentableTypeTestCase(TestCase):
    """Tests the Fermentable Type Model"""

    def test_create_fermentable_type(self):
        """Tests that a fermentable type can be created and queried"""
        TestFactory.create_fermentable_type()
        self.assertIsNotNone(FermentableType.objects.get(name="Test Grain"))

    def test_fermentable_type_str_method(self):
        """Tests str(FermentableType) returns expected value"""
        test_fermentable_type = TestFactory.create_fermentable_type()
        self.assertEqual(
            str(test_fermentable_type),
            test_fermentable_type.name
        )


class FermentableTestCase(TestCase):
    """Tests the Fermentable Model"""

    def test_create_fermentable(self):
        """Tests basic fermentable creation"""
        TestFactory.create_fermentable()
        self.assertIsNotNone(Fermentable.objects.get(name="Test Fermentable"))

    def test_fermentable_str_method(self):
        """Tests str(Fermentable) returns expected value"""
        test_fermentable = TestFactory.create_fermentable()
        self.assertEqual(
            str(test_fermentable),
            test_fermentable.name
        )

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
