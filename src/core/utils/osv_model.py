"""Defines The API Model data"""


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
