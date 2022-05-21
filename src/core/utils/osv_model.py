"""Defines The API Model data"""

from src.core.utils.generics.url_model import Url


class OsvModel:
    """Model to be used for fetch the OSV api

    It replaces the `package` and `version` parameters
    and post-processes the data to a string that the API can read.
    """

    def __init__(self, package: str, version: str):
        self.package = package
        self.version = version

    def get_data(self) -> str:
        model = str(
            {
                "version": self.version,
                "package": {"name": self.package, "ecosystem": "PyPI"},
            }
        )
        return model


class OsvUrl(Url):
    """Just the OSV url"""

    def __init__(self):
        self.url = "https://api.osv.dev/v1/query"

    def get_url(self):
        return self.url
