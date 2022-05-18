"""Fetch the OSV API"""

from pprint import pprint
import requests

from models.osv_model import OsvModel, OsvUrl


def fetch_api(osv_model: OsvModel) -> dict:
    """Fetch the OSV API"""

    osv_link = OsvUrl().get_url()
    osv_model = osv_model.get_data()

    response = requests.post(osv_link, data=osv_model)

    return response.json()
