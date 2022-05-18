"""Filters results from OSV API
"""

from models.utils.flatten_list import flatten_list


class FilterByReport:
    """Filters results from OSV API"""

    @staticmethod
    def get_report_id(report: dict) -> str:
        return report["id"]

    @staticmethod
    def get_report_summary(report: dict) -> str:
        return report["summary"]

    @staticmethod
    def get_report_description(report: dict) -> str:
        return report["details"]

    @staticmethod
    def get_report_aliases(report: dict) -> list:
        return report["aliases"]

    @staticmethod
    def get_report_affected_versions(report: dict) -> list:
        versions_arrays = [sub["versions"] for sub in report["affected"]]
        return flatten_list(versions_arrays)
