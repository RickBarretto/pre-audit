"""Fetch the OSV API"""

import requests
from requests.exceptions import HTTPError

from src.core.utils.osv_model import OsvModel, OsvUrl


def fetch_api(osv_model: OsvModel) -> dict:
    """Fetch the OSV API and return a Json"""

    osv_link = OsvUrl().get_url()
    osv_model = osv_model.get_data()

    response = requests.post(osv_link, data=osv_model)
    response.raise_for_status()
    json = response.json()

    return json
