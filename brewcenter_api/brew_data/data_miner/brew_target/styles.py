from brew_data.data_miner.brew_target.utils import clean

class Style:
    def __init__(self, data):
        self.name = data[0]
        self.type = data[1]
        self.category = data[2]
        self.og_min = data[3]
        self.og_max = data[4]
        self.fg_min = data[5]
        self.fg_max = data[6]
        self.ibu_min = data[7]
        self.ibu_max = data[8]
        self.srm_min = data[9]
        self.srm_max = data[10]
        self.abv_min = data[11]
        self.abv_max = data[12]
        self.transform()

    def transform(self):
        self.name = '"' + self.name + '"'
        self.type = '"' + self.type + '"'
        self.category = '"' + self.category + '"'

    def get_keys():
        return "name, type, category, og_min, og_max, fg_min, fg_max, ibu_min, ibu_max, srm_min, srm_max, abv_min, abv_max"

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}".format(
            self.name,
            self.type, 
            self.category, 
            self.og_min, 
            self.og_max, 
            self.fg_min, 
            self.fg_max, 
            self.ibu_min, 
            self.ibu_max, 
            self.srm_min, 
            self.srm_max, 
            self.abv_min, 
            self.abv_max
        )


def get_styles(s, d, stdout):
    """
    Gets yeast from the source database (s), transforms them,
    and puts them in the destination database (d)
    """
    n = 0

    d.execute('DROP TABLE IF EXISTS styles;')
    d.execute('CREATE TABLE styles(' \
        'name TEXT,'                 \
        'type TEXT,'                 \
        'category TEXT,'             \
        'og_min FLOAT,'              \
        'og_max FLOAT,'              \
        'fg_min FLOAT,'              \
        'fg_max FLOAT,'              \
        'ibu_min FLOAT,'             \
        'ibu_max FLOAT,'             \
        'srm_min FLOAT,'             \
        'srm_max FLOAT,'             \
        'abv_min FLOAT,'             \
        'abv_max FLOAT'              \
        ');'
    )

    s.execute('SELECT "name", "type", "category", "og_min", "og_max", "fg_min", "fg_max", "ibu_min", "ibu_max", "color_min", "color_max", "abv_min", "abv_max" FROM style WHERE `deleted`=0;') 
    cur = s.fetchone()
    while cur:
        style = Style(cur)
        d.execute('INSERT INTO styles({0}) VALUES({1});'.format(Style.get_keys(), style))
        n+=1
        cur = s.fetchone()

    print("Found {0} styles.".format(n))