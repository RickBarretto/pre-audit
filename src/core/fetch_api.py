"""Fetch the OSV API"""

import requests
from requests.exceptions import HTTPError

from src.core.utils.osv_model import OsvModel
from src.core.utils.exceptions import PackageNotFound


import requests


class OsvApi:
    """Deal with OsvApi to get package Vulnerabilities

    usage:
    >>> OsvApi("Django", "3.0").fetch()
    {...}
    """

    def __init__(self, package: str, version: str):

        # Attributes
        self.api_parameters = OsvModel(package, version).get_data()

    def fetch(self):
        json: dict = self.__request()
        if json:
            return json
        else:
            raise PackageNotFound

    def __request(self) -> dict:
        """Fetch the OSV API and return a Json"""

        osv_link = "https://api.osv.dev/v1/query"

        response = requests.post(osv_link, data=self.api_parameters, timeout=3.05)
        response.raise_for_status()

        json = response.json()

        return json
