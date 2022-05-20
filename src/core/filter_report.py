"""Filters results from OSV API
"""

from src.core.utils.flatten_list import flatten_list
from src.core.utils.generics.index_model import Index


class FilterByReport:
    """Filters results from OSV API by report

    - What are Reports?
    When fetches the OSV API, it comes with a dict and a `vulns` item inside.
    `vulns` is a list with reports, and each item is one report.

    Methods:
        - def get_id(report: dict) -> str:
        - def get_summary(report: dict) -> str:
        - def get_description(report: dict) -> str:
        - def get_aliases(report: dict) -> list:
        - def get_affected_versions(report: dict) -> list:
        - def get_references(report: dict) -> list:
    """

    def __init__(self, fetched_data: dict):
        self.reports: list = fetched_data.get("vulns")

    def get_main_info(self):
        """Get the ID and Detail from each report"""
        return [(report["id"], report["details"]) for report in reports]

    def get_all_affected_versions(self) -> list:
        versions_arrays = [sub["affected"]["versions"] for sub in self.reports]
        return flatten_list(versions_arrays)

    def get_id(report: Index) -> str:
        return report["id"]

    def get_summary(report: Index) -> str:
        return report["summary"]

    def get_description(report: Index) -> str:
        return report["details"]

    def get_aliases(report: Index) -> list:
        return report["aliases"]

    def get_references(report: Index) -> list:
        return report["references"]
