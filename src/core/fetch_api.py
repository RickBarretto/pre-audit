"""Fetch the OSV API"""

import requests
from requests.exceptions import HTTPError

from src.core.utils.osv_model import OsvModel, OsvUrl
from src.core.utils.exceptions import PackageNotFound


import requests


class OsvApi:
    """Deal with OsvApi to get package Vulnerabilities

    usage:
    >>> django_pkg = OsvModel("Django", "3.0")
    >>> response = OsvApi(django_pkg).fetch()
    {...}
    """

    def __init__(self, osv_parameters: OsvModel):

        # Attributes
        self.api_parameters = osv_parameters.get_data()

    def fetch(self):
        json: dict = self.__request()
        if json:
            return json
        else:
            raise PackageNotFound

    def __request(self) -> dict:
        """Fetch the OSV API and return a Json"""

        osv_link = "https://api.osv.dev/v1/query"

    response = requests.post(osv_link, data=osv_model)
    response.raise_for_status()
    json = response.json()

    return json


def raise_for_not_found(json: dict):
    if not json:
        raise PackageNotFound
