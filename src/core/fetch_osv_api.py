from pprint import pprint
import requests

from src.models.osv_model import OsvModel, OsvUrl


def fetch_api(package: str, version: str) -> dict:

    osv_link = OsvUrl().get_url()
    osv_model = OsvModel(package, version).get_data()

    response = requests.post(osv_link, data=osv_model)

    return response.json()
