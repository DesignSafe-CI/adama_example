# -*- coding: utf-8 -*-

import csv
import os
import re


HERE = os.path.dirname(os.path.abspath(__file__))


def sexa_to_dec(dh, min, secs, sign):
    return sign*(dh + float(min)/60 + float(secs)/60**2)


def string_to_dec(s, neg):
    parsed = filter(
        None, re.split('[\'" °]', unicode(s, 'utf-8')))
    sign = -1 if parsed[-1] == neg else 1
    return sexa_to_dec(float(parsed[0]), float(parsed[1]), float(parsed[2]),
                       sign)


def process_geo_coordinates(obj):
    if obj['Latitude']:
        obj['Latitude'] = string_to_dec(obj['Latitude'], 'S')
    if obj['Longitude']:
        obj['Longitude'] = string_to_dec(obj['Longitude'], 'W')


def load_db():
    with open(os.path.join(HERE, 'The_Haiti_Earthquake_Database.csv')) as f:
        reader = csv.DictReader(f)
        for elt in reader:
            del elt['']
            process_geo_coordinates(elt)
            yield elt


HAITI_DB = list(load_db())


