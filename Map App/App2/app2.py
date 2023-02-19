import sys
from io import BytesIO
import requests
from PIL import Image
from module1 import get_size


def show_organization(object):
    x, y = object["geometry"]["coordinates"]
    map_params = {
        "ll": f"{x},{y}",
        "spn": get_size(object),
        "l": "map",
        "pt": f"{x},{y},pm2dgl"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    if not response:
        sys.exit(2)

    Image.open(BytesIO(response.content)).show()


def find_organization(name="аптека", point="37.588392,55.734036"):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

    search_params = {
        "apikey": api_key,
        "text": name,
        "lang": "ru_RU",
        "ll": point,
        "type": "biz"
    }

    response = requests.get(search_api_server, params=search_params)

    if not response:
        sys.exit(1)

    json_response = response.json()

    try:
        organization = json_response["features"][0]
    except IndexError:
        sys.exit(3)

    show_organization(organization)


find_organization(input())
