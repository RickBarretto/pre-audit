"""Fetch the OSV API"""

import requests

from src.core.utils.osv_model import OsvModel, OsvUrl


def fetch_api(osv_model: OsvModel) -> dict:
    """Fetch the OSV API and return a Json"""

    osv_link = OsvUrl().get_url()
    osv_model = osv_model.get_data()

    response = requests.post(osv_link, data=osv_model)

    return response.json()
