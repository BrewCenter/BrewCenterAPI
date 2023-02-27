from django.core.management.base import BaseCommand, CommandError
# from polls.models import Question as Poll
from ingredients.models import FermentableBase, Grain, GrainType, FermentableType, Origin, Manufacturer
import json
import brutils
import pycountry

def get_in(dic, keys):
	cur = dic
	for i in range(0, len(keys)):
		key = keys[i]
		if type(cur) is dict and key not in cur:
			return None
		elif cur and type(cur) is dict and key in cur:
			cur = cur[key]
		elif i != len(keys) - 1:
			cur = None

	return cur

def transform_percent(percent_out_of_100):
	if percent_out_of_100 is None:
		return None
	return float(percent_out_of_100)/100

class Command(BaseCommand):
	help = 'Imports ingredients from a beer_json file'

	def add_arguments(self, parser):
		parser.add_argument('beer_json_file', nargs=1, type=open)

	def handle(self, *args, **options):
		beer_json = options['beer_json_file'][0].read()

		try:
			beer_json = json.loads(beer_json)
		except:
			raise CommandError('Unable to load beer_json file. Make sure the file is properly formatted json.')

		if 'fermentables' in beer_json:
			for fermentable in beer_json['fermentables']:
				print('importing ' + fermentable['name'])
				ferm_type = FermentableType.objects.get(value=fermentable['type'])
				potential_ppg = brutils.sg_to_ppg(get_in(fermentable, ['yield', 'potential', 'value']))
				origin_name = get_in(fermentable, ['origin'])
				country = None
				if len(origin_name) == 2:
					country = pycountry.countries.get(alpha_2=origin_name)
				elif len(origin_name) == 3:
					country = pycountry.countries.get(alpha_3=origin_name)
				else:
					country = pycountry.countries.get(alpha_2=input('Enter the iso 2 country code for ' + origin_name))

				origin = Origin.objects.get_or_create(name=origin_name, country_code=country.alpha_3)[0]
				manufacturer = Manufacturer.objects.get_or_create(name=get_in(fermentable, ['producer']))[0]

				fbase = FermentableBase.objects.update_or_create(
					name=fermentable['name'],
					type=ferm_type,
					is_active=True,
					potential_ppg=potential_ppg,
					product_id=get_in(fermentable, ['product_id']),
					origin=origin,
					manufacturer=manufacturer,
					color_srm=get_in(fermentable, ['color', 'value']),
					notes=get_in(fermentable, ['notes']),
					fermentability_percent=transform_percent(get_in(fermentable, ['fermentability', 'value'])),
				)[0]

				if ferm_type.value == 'grain':
					grain_type = GrainType.objects.get(name__iexact=get_in(fermentable, ['grain_group']))

					Grain.objects.update_or_create(
						type=grain_type,
						fermentable=fbase,
						alpha_amylase=get_in(fermentable, ['alpha_amylase']),
						diastatic_power_lintner=get_in(fermentable, ['diastatic_power', 'value']),
						viscosity_cp=get_in(fermentable, ['viscosity', 'value']),
						fan_mg_l=get_in(fermentable, ['fan', 'value']),
						moisture_percent=transform_percent(get_in(fermentable, ['moisture', 'value'])),
						fine_grind_potential_percent=transform_percent(get_in(fermentable, ['yield', 'fine_grind', 'value'])),
						coarse_grind_potential_percent=transform_percent(get_in(fermentable, ['yield', 'coarse_grind', 'value'])),
						protein_percent=transform_percent(get_in(fermentable, ['protein', 'value'])),
						kolbach_index_percent=transform_percent(get_in(fermentable, ['kolbach_index'])),
						max_in_batch_percent=transform_percent(get_in(fermentable, ['max_in_batch', 'value'])),
						plump_percent=transform_percent(get_in(fermentable, ['plump', 'value'])),
						glassy_percent=transform_percent(get_in(fermentable, ['glassy', 'value'])),
						half_percent=transform_percent(get_in(fermentable, ['half', 'value'])),
						mealy_percent=transform_percent(get_in(fermentable, ['mealy', 'value'])),
						thru_percent=transform_percent(get_in(fermentable, ['thru', 'value'])),
						friability_percent=transform_percent(get_in(fermentable, ['friability', 'value'])),
					)
