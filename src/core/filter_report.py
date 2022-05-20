"""Filters results from OSV API
"""

from typing import List

from src.core.utils.flatten_list import flatten_list
from src.core.utils.generics.generic_models import Index


class FilterByReport:
    """Filters results from OSV API by report

    - What are Reports?
    When fetches the OSV API, it comes with a dict and a `vulns` item inside.
    `vulns` is a list with reports, and each item is one report.

    Methods:
        - get_main_info(self) -> list[ tuple[ReportId, ReportDescription] ]
        - get_all_affected_versions(self) -> ReportVersions
        - get_id(self, report: Index) -> ReportId
        - get_summary(self, report: Index) -> ReportSummary
        - get_description(self, report: Index) -> ReportDescription
        - get_aliases(self, report: Index) -> ReportAliases
        - get_affected_versions(self, report: Index) -> ReportVersions
        - get_references(self, report: Index) -> ReportReferences
    """

    def __init__(self, fetched_data: dict):
        self.reports: list = fetched_data.get("vulns")

    def get_main_info(self) -> List[tuple[ReportId, ReportDescription]]:
        """Get the ID and Detail from all reports"""
        return [(report["id"], report["details"]) for report in reports]

    def get_all_affected_versions(self) -> ReportVersions:
        """Get all affected versions from all reports"""
        versions_arrays = [sub["affected"]["versions"] for sub in self.reports]
        return flatten_list(versions_arrays)

    def get_id(self, report: Index) -> ReportId:
        """Get a specific report's id"""
        return report["id"]

    def get_summary(self, report: Index) -> ReportSummary:
        """Get a specific report's summary"""
        return report["summary"]

    def get_description(self, report: Index) -> ReportDescription:
        """Get a specific report's description"""
        return report["details"]

    def get_aliases(self, report: Index) -> ReportAliases:
        """Get a specific report's aliases"""
        return report["aliases"]

    def get_references(self, report: Index) -> ReportReferences:
        """Get a specific report's references"""
        return report["references"]
