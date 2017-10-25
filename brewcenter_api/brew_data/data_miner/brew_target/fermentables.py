"""
Extracts Fermentables from the database, transforms them, and builds a new db.
"""

from brew_data.data_miner.brew_target.utils import clean, convert_country


class Fermentable:
    def __init__(self, data):
        self.name = data[0]
        self.type = data[1]
        self.potential = data[2]
        self.lovibond = data[3]
        self.origin = data[4]
        self.supplier = data[5]
        self.notes = clean(data[6])
        self.coarse_fine_diff = data[7]
        self.moisture = data[8]
        self.diastatic_power = data[9]
        self.protein = data[10]
        self.max_in_batch = data[11]
        self.is_mashed = data[12]

        self.transform()

    def transform(self):
        """transforms the data as neccessary to fit our specs"""
        self.name = '"' + self.name + '"'
        # convert boolean to integer for sqlite
        self.is_mashed = (1 if self.is_mashed == 'true' else 0)
        # Sugar has a PPG of 46. Multiply the potential percent yield by 46 to
        # get PPG of a grain
        self.ppg = 46 * (self.potential / 100)

        self.country = convert_country(self.origin)

        # parse type
        if self.type == "Extract":
            self.type = "Liquid Malt Extract"
        elif self.type == "Dry Extract":
            self.type = "Dry Malt Extract"

        if len(self.type) == 0:
            self.type = "NULL"
        else:
            self.type = '"' + self.type + '"'

        # convert "None" notes to empty
        if self.notes is None:
            self.notes = '""'
        else:
            self.notes = '"' + self.notes + '"'

    def get_keys():
        return ("name, type_id, country_id, notes, ppg, lovibond, moisture, "
                "diastatic_power, protein, max_in_batch, is_mashed")

    def __str__(self):
        format_str = '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'
        return format_str.format(
            self.name,
            self.type_id,
            self.country_id,
            self.notes,
            self.ppg,
            self.lovibond,
            self.moisture,
            self.diastatic_power,
            self.protein,
            self.max_in_batch,
            self.is_mashed,
        )


def get_fermentables(s, d):
    """
    Gets fermentables from the source (s) and puts them in the destination (d).
    """
    d.execute('DROP TABLE IF EXISTS fermentabletype;')
    d.execute('DROP TABLE IF EXISTS fermentable;')
    d.execute('CREATE TABLE fermentabletype(name TEXT, abbreviation TEXT);')
    d.execute('CREATE TABLE fermentable('  \
        'name TEXT,'                       \
        'type_id int,'                     \
        'country_id int,'                  \
        'ppg FLOAT,'                       \
        'lovibond FLOAT,'                  \
        'moisture FLOAT,'                  \
        'diastatic_power FLOAT,'           \
        'protein FLOAT,'                   \
        'max_in_batch FLOAT,'              \
        'is_mashed INT,'                   \
        'notes TEXT'                       \
        ');'
    )
    s.execute('SELECT "name", "ftype", "yield", "color", "origin", "supplier", "notes", "coarse_fine_diff", "moisture", "diastatic_power", "protein", "max_in_batch", "is_mashed" FROM fermentable WHERE `deleted`=0;') 
    cur = s.fetchone()
    n = 0
    while cur:
        f = Fermentable(cur)

        # check if the country code exists already and add it if it does not
        f.country_id = 'NULL'
        if f.country is not 'NULL':
            d.execute('SELECT `rowid` FROM countrycode WHERE code={0};'.format(f.country))
            country_code_id = d.fetchone()
            if country_code_id is None:
                d.execute('INSERT INTO countrycode(code) VALUES ({0});'.format(f.country))
                d.execute('SELECT `rowid` FROM countrycode WHERE code={0};'.format(f.country))
                country_code_id = d.fetchone()
            f.country_id = country_code_id[0] if country_code_id else 'NULL'

        # check if the type already exists and add it if it does not
        f.type_id = 'NULL'
        if f.type is not 'NULL':
            d.execute('SELECT `rowid` FROM fermentabletype WHERE name={0};'.format(f.type))
            type_id = d.fetchone()
            if type_id is None:
                d.execute('INSERT INTO fermentabletype(name) VALUES({0});'.format(f.type))
                d.execute('SELECT `rowid` FROM fermentabletype WHERE name={0};'.format(f.type))
                type_id = d.fetchone()
            f.type_id = type_id[0] if type_id else 'NULL'

        query = 'INSERT INTO fermentable({0}) VALUES({1});'.format(Fermentable.get_keys(), str(f))
        d.execute(query)
        n += 1
        cur = s.fetchone()
    print("Found {0} fermentables.".format(n))
