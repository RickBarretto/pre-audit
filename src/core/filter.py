"""Filters results from OSV API
"""


class FilterForOsvVulns:
    """Filters results from OSV API"""

    def __init__(self, raw_data: dict):
        data = self.__fetch(raw_data)
        self.data = data

    def __fetch(self, raw_data: dict) -> list:
        """Returns a unfiltred list of Vulnerabilities"""

        return raw_data.get("vulns")

    def get_vulnerabilities(self) -> list:
        """Returns a filtred list of Vulnerabilities

        returns:
            id,
            description,
            affected
        """

        reports = [reports for reports in self.data]

        return [
            {"id": r["id"], "description": r["details"], "affected": r["affected"]}
            for r in reports
        ]

    def get_blacklisted_versions(self) -> list:
        """Returns a list of problematic versions"""
        pass
