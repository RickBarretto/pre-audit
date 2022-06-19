"""Deals with core functions"""

from src.core.fetch_api import OsvApi
from src.core.filter_report import Filter


def fetch(package: str, version: str) -> list:
    """Fetches the data from OsvApi"""
    return Filter(OsvApi(package, version).fetch())


def get_main_info(filtred_data: Filter) -> list:
    """Get the main info to print"""
    return filtred_data.get_main_info()


def get_all_affected_versions_info(filtred_data: Filter) -> list:
    """Gets all affected version"""
    return filtred_data.get_all_affected_versions()
