"""Various functions for cleaning and transforming data."""

import pycountry


def convert_country(country_name):
    """Converts a country name to a code."""
    c = ""
    country = None
    try:
        country = pycountry.countries.get(name=country_name)
        c = country.alpha_2
    except:
        c = country_name
    if c is None or len(c) == 0:
        c = "NULL"
    else:
        c = '"' + c + '"'
    return c


def clean(data):
    if "\"" in str(data):
        data = data.replace("\"", "\"\"")
    return data
