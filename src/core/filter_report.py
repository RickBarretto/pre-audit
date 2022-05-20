"""Filters results from OSV API
"""

from typing import List, Dict

from src.core.utils.flatten_list import flatten_list


class FilterByReport:
    """Filters results from OSV API by report

    - What are Reports?
    When fetches the OSV API, it comes with a dict and a `vulns` item inside.
    `vulns` is a list with reports, and each item is one report.

    Methods:
        - get_main_info(self) -> list[ tuple[str, str] ]
        - get_all_affected_versions(self) -> list[str]
        - get_id(self, report_index: int) -> str
        - get_summary(self, report_index: int) -> str
        - get_description(self, report_index: int) -> str
        - get_aliases(self, report_index: int) -> list[str]
        - get_affected_versions(self, report_index: int) -> list[str]
        - get_references(self, report_index: int) -> list[dict[str, str]]
    """

    def __init__(self, fetched_data: dict):
        self.reports: list = fetched_data.get("vulns")

    def get_main_info(self) -> List[tuple[str, str]]:
        """Get the ID and Detail from all reports"""
        return [(report["id"], report["details"]) for report in self.reports]

    def get_all_affected_versions(self) -> List[str]:
        """Get all affected versions from all reports"""
        versions_arrays = [sub["affected"]["versions"] for sub in self.reports]
        return flatten_list(versions_arrays)

    def get_id(self, report_index: int) -> str:
        """Get a specific report's id"""
        return self.reports[report_index]["id"]

    def get_summary(self, report_index: int) -> str:
        """Get a specific report's summary"""
        return self.reports[report_index]["summary"]

    def get_description(self, report_index: int) -> str:
        """Get a specific report's description"""
        return self.reports[report_index]["details"]

    def get_aliases(self, report_index: int) -> List[str]:
        """Get a specific report's aliases"""
        return self.reports[report_index]["aliases"]

    def get_references(self, report_index: int) -> List[Dict[str, str]]:
        """Get a specific report's references"""
        return self.reports[report_index]["references"]
