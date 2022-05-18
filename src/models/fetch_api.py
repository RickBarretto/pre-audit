"""Fetch the OSV API"""
import requests

from models.types.osv_model import OsvModel, OsvUrl


def fetch_api(osv_model: OsvModel) -> dict:
    """Fetch the OSV API"""

    osv_link = OsvUrl().get_url()
    osv_model = osv_model.get_data()

    response = requests.post(osv_link, data=osv_model)

    return response.json()
