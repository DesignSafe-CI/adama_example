import csv
import os


HERE = os.path.dirname(os.path.abspath(__file__))


def load_db():
    with open(os.path.join(HERE, 'The_Haiti_Earthquake_Database.csv')) as f:
        reader = csv.DictReader(f)
        for elt in reader:
            del elt['']
            yield elt


HAITI_DB = list(load_db())


