"""Filters results from OSV API
"""

from models.utils.flatten_list import flatten_list


class FilterByReport:
    """Filters results from OSV API"""

    @staticmethod
    def get_id(report: dict) -> str:
        return report["id"]

    @staticmethod
    def get_summary(report: dict) -> str:
        return report["summary"]

    @staticmethod
    def get_description(report: dict) -> str:
        return report["details"]

    @staticmethod
    def get_aliases(report: dict) -> list:
        return report["aliases"]

    @staticmethod
    def get_affected_versions(report: dict) -> list:
        versions_arrays = [sub["versions"] for sub in report["affected"]]
        return flatten_list(versions_arrays)

    @staticmethod
    def get_references(report: dict) -> list:
        return report["references"]
