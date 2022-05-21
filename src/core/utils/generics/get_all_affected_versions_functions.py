"""Internal functions of `get_all_affected_versions` method

There are just the logic behind this method
from `src.core.filter_report.Filter`
"""

from src.core.utils.flatten_list import flatten_list


class AllAffectedVersions:
    @staticmethod
    def _affected_dict(reports) -> dict:
        """Returns the affected dictionary from reports"""
        return [report["affected"] for report in reports]

    @staticmethod
    def get(reports) -> list:
        """Returns all affected versions from reports"""
        affected_reports = AllAffectedVersions._affected_dict(reports)
        not_flatten = [a["versions"] for sublist in affected_reports for a in sublist]
        return flatten_list(not_flatten)
