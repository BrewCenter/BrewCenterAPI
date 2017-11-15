from django.test import TestCase
from ..models.style import Style


class StyleTest(TestCase):
    """
    Test module for types of beer
    """
    def setUp(self):
        Style.objects.create(id='101', name='De Koninick', 
                             type="Ale", category='brown',
                             og_min=1.044, og_max=1.054,
                             fg_min=1.008, fg_max=1.014,
                             ibu_min=20, ibu_max=30,
                             srm_min=3, srm_max=5, 
                             abv_min=3.2, abv_max=5)

        Style.objects.create(id='102', name='Alaskan Auntumn Ale', 
                             type="Ale", category='pale',
                             og_min=1.044, og_max=1.056,
                             fg_min=1.008, fg_max=1.016,
                             srm_min=5, srm_max=7, 
                             abv_min=3, abv_max=4.5)

        Style.objects.create(id='103', name='Budweiser',
                             type="Lager", category='blonde',
                             og_min=1.075, og_max=1.085,
                             fg_min=1.006, fg_max=1.012, 
                             ibu_min=40, ibu_max=50,
                             srm_min=6, srm_max=9,
                                abv_min=5, abv_max=8)

    def test_style_name(self):
        ale = Style.objects.get(id='101') 
        lager = Style.objects.get(id='103')

        self.assertEqual(ale.name, 'De Koninick')
        self.assertEqual(lager.name, 'Budweiser')
  
    
