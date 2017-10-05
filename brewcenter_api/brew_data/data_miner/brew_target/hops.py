from brew_data.data_miner.brew_target.utils import clean, convert_country


class Hop:
    def __init__(self, data):
        self.name = data[0]
        self.type = data[1]
        self.origin = data[2]
        self.alpha_acids = data[3]
        self.beta_acids = data[4]
        self.notes = clean(data[5])
        self.transform()

    def transform(self):
        self.name = '"' + self.name + '"'
        self.type = '"' + self.type + '"'
        # convert "None" notes to empty
        if self.notes is None:
            self.notes = '""'
        else:
            self.notes = '"' + self.notes + '"'

        # change countries to valid ones
        lookup = {
            "England": "UK",
            "Czech Republic": "CZ",
            "Austria/Slovenia": "AT"
        }
        if self.origin in lookup:
            self.origin = lookup[self.origin]

        self.country = convert_country(self.origin)

    def get_keys():
        return "name, type_id, country_id, alpha_acids, beta_acids, notes"

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5}".format(
            self.name,
            self.type_id,
            self.country_id,
            self.alpha_acids,
            self.beta_acids,
            self.notes
        )


def get_hops(s, d, stdout):
    """
    Gets hops rom the source database (s), transforms them,
    and puts them in the destination database (d)
    """
    n = 0

    d.execute('DROP TABLE IF EXISTS hoptype;')
    d.execute('DROP TABLE IF EXISTS hop;')
    d.execute('CREATE TABLE hoptype(name TEXT);')
    d.execute('CREATE TABLE hop('  \
        'name TEXT,'                \
        'type_id int,'              \
        'country_id int,'           \
        'alpha_acids FLOAT,'        \
        'beta_acids FLOAT,'         \
        'notes TEXT'                \
        ');'
    )

    s.execute('SELECT "name", "htype", "origin", "alpha", "beta", "notes" FROM hop WHERE `deleted`=0;') 
    cur = s.fetchone()
    while cur:
        h = Hop(cur)

        # check for the country code and set it's foreign id
        h.country_id = 'NULL'
        if h.country is not 'NULL':
            d.execute('SELECT `rowid` FROM countrycode WHERE code={0};'.format(h.country))
            country_code_id = d.fetchone()
            if country_code_id is None:
                d.execute('INSERT INTO countrycode(code) VALUES ({0});'.format(h.country))
                d.execute('SELECT `rowid` FROM countrycode WHERE code={0};'.format(h.country))
                country_code_id = d.fetchone()
            h.country_id = country_code_id[0] if country_code_id else 'NULL'

        # check for the hop type set it's foreign id
        h.type_id = 'NULL'
        if h.type is not 'NULL':
            d.execute('SELECT `rowid` FROM hoptype WHERE name={0};'.format(h.type))
            hop_type_id = d.fetchone()
            if hop_type_id is None:
                d.execute('INSERT INTO hoptype(name) VALUES ({0});'.format(h.type))
                d.execute('SELECT `rowid` FROM hoptype WHERE name={0};'.format(h.type))
                hop_type_id = d.fetchone()
            h.type_id = hop_type_id[0] if hop_type_id else 'NULL'

        d.execute('INSERT INTO hop({0}) VALUES({1});'.format(Hop.get_keys(), h))
        n+=1
        cur = s.fetchone()

    print("Found {0} hops.".format(n))
