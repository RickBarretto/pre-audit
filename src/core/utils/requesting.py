import requests


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


def fetch(api_parameters: OsvModel) -> dict:
    """Fetch the OSV API and return a Json"""

    osv_link = "https://api.osv.dev/v1/query"

    response = requests.post(osv_link, data=api_parameters, timeout=3.05)
    response.raise_for_status()

    json = response.json()

    return json
