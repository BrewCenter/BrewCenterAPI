import sqlite3 as sql
import sys
import os

from brew_data.data_miner.brew_target.fermentables import Fermentable, get_fermentables
from brew_data.data_miner.brew_target.hops import Hop, get_hops
from brew_data.data_miner.brew_target.yeast import Yeast, get_yeast
from brew_data.data_miner.brew_target.styles import Style, get_styles

def mine(stdout):
    DIR = os.path.dirname(os.path.abspath(__file__))
    source = sql.connect(os.path.join(DIR, 'brewtarget.sqlite'))
    dest = sql.connect(os.path.join(DIR, 'brewtarget_processed.sqlite'))
    s = source.cursor()
    d = dest.cursor()

    args = sys.argv

    do_fermentables = False
    do_hops = False
    do_yeast = False
    do_styles = False

    if "fermentables" in args:
        do_fermentables = True
    if "hops" in args:
        do_hops = True
    if "yeast" in args:
        do_yeast = True
    if "styles" in args:
        do_styles = True

    if not do_hops and not do_fermentables and not do_yeast and not do_styles:
        do_fermentables = True
        do_hops = True
        do_yeast = True
        do_styles = True

    if do_hops or do_fermentables:
        d.execute('DROP TABLE IF EXISTS countrycode;')
        d.execute('CREATE TABLE countrycode(code TEXT);')

    if do_fermentables:
        get_fermentables(s, d)

    if do_hops:
        get_hops(s, d, stdout)

    if do_yeast:
        get_yeast(s, d, stdout)

    if do_styles:
        get_styles(s, d, stdout)

    source.close()
    dest.commit()
    dest.close()

if __name__ == '__main__':
    mine();