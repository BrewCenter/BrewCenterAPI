import itertools
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from iso3166 import countries_by_alpha3, countries_by_alpha2


def country_code_validator(value):
    all_countries = [{'code':i} for i in itertools.chain(countries_by_alpha3,countries_by_alpha2)]
    if str(value).upper() not in all_countries:
        raise ValidationError(_('%(code) is not a valid country code.'),params={'code':value})