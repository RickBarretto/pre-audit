"""Defines The API Model data"""


class OsvModel:
    def __init__(self, package: str, version: str):
        self.package = package
        self.version = version

    def get_data(self) -> str:
        model = str(
            {"version": version, "package": {"name": package, "ecosystem": "PyPI"}}
        )
        return model


class OsvUrl(Url):
    def __init__(self):
        self.url = "https://api.osv.dev/v1/query"

    def get_url(self):
        return self.url
