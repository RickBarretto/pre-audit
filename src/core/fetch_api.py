"""Fetch the OSV API"""

import requests
from requests.exceptions import HTTPError

from src.core.utils import requesting
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
        self.api_parameters = requesting.OsvModel(package, version).get_data()

    def fetch(self):
        json: dict = requesting.fetch(self.api_parameters)
        if json:
            return json
        else:
            raise PackageNotFound
