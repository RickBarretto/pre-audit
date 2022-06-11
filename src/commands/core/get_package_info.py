from src.core.fetch_api import OsvApi
from src.core.filter_report import Filter


def get_package_info(package: str, version: str) -> list:
    data = OsvApi(package, version).fetch()
    return Filter(data).get_main_info()
