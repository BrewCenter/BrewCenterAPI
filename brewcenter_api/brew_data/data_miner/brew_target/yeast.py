from brew_data.data_miner.brew_target.utils import clean


class Yeast:
    def __init__(self, data):
        self.name = data[0]
        self.type = data[1]
        self.form = data[2]
        self.lab = data[3]
        self.min_temp = data[4]
        self.max_temp = data[5]
        self.flocculation = data[6]
        self.attenuation = data[7]
        self.notes = clean(data[8])
        self.transform()

    def transform(self):
        self.name = '"' + self.name + '"'
        self.type = '"' + self.type + '"'
        self.lab = '"' + self.lab + '"'
        self.flocculation = '"' + self.flocculation + '"'
        # convert "None" notes to empty
        if self.notes is None:
            self.notes = '""'
        else:
            self.notes = '"' + self.notes + '"'

        self.is_liquid = 0
        if self.form == "Liquid":
            self.is_liquid = 1

    def get_keys():
        return ("name, type_id, is_liquid, lab, min_temp, max_temp, "
                "flocculation, attenuation, notes")

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8}".format(
            self.name,
            self.type_id,
            self.is_liquid,
            self.lab,
            self.min_temp,
            self.max_temp,
            self.flocculation,
            self.attenuation,
            self.notes,
        )


def get_yeast(s, d, stdout):
    """
    Get yeast from the source database (s), transform them,
    and put them in the destination database (d)
    """
    n = 0

    d.execute('DROP TABLE IF EXISTS yeasttype;')
    d.execute('DROP TABLE IF EXISTS yeast;')
    d.execute('CREATE TABLE yeasttype(name TEXT);')
    d.execute('CREATE TABLE yeast('
              'name TEXT,'
              'type_id int,'
              'is_liquid int,'
              'lab TEXT,'
              'min_temp FLOAT,'
              'max_temp FLOAT,'
              'flocculation FLOAT,'
              'attenuation FLOAT,'
              'notes TEXT'
              ');')

    s.execute('SELECT "name", "ytype", "form", "laboratory", "min_temperature", "max_temperature", "flocculation", "attenuation", "notes" FROM yeast WHERE `deleted`=0;')
    cur = s.fetchone()
    while cur:
        y = Yeast(cur)

        # check for the yeast type and set it's foreign id
        y.type_id = 'NULL'
        if y.type is not 'NULL':
            d.execute('SELECT `rowid` FROM yeasttype WHERE name={0};'.format(y.type))
            yeast_type_id = d.fetchone()
            if yeast_type_id is None:
                d.execute('INSERT INTO yeasttype(name) VALUES ({0});'.format(y.type))
                d.execute('SELECT `rowid` FROM yeasttype WHERE name={0};'.format(y.type))
                yeast_type_id = d.fetchone()
            y.type_id = yeast_type_id[0] if yeast_type_id else 'NULL'

        d.execute('INSERT INTO yeast({0}) VALUES({1});'.format(Yeast.get_keys(), y))
        n += 1
        cur = s.fetchone()

    print("Found {0} yeast.".format(n))
