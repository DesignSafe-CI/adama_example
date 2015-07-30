import json

import requests


BASE_LINK = ('https://nees.org/site/collections/haiti/Pictures'
             '/{id}/{id}%20-%20({index}).JPG')


def search(args, adama):
    """Search images by building id."""

    building_id = args['building']
    index = args.get('image', 1)
    url = BASE_LINK.format(id=building_id, index=index)
    return 'image/jpeg', requests.get(url).content
