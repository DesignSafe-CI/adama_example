import json

import services.common.tools as t


def search(args, adama):
    """Search database by building id."""

    building_id = args['building']
    for row in t.HAITI_DB:
        if row['Building'].startswith(building_id):
            print json.dumps(row, indent=4)
            print '---'
        

def list(args, adama):
    """List all rows."""

    for row in t.HAITI_DB:
        print json.dumps(row, indent=4)
        print '---'
