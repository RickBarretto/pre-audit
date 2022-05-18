"""Filters results from OSV API
"""


class FilterForOsvVulns:
    """Filters results from OSV API"""

    def __init__(self, raw_data: dict):
        data = __fetch(raw_data)
        self.data = data

    def __fetch(self, raw_data: dict) -> list:
        """Returns a unfiltred list of Vulnerabilities"""

        return raw_data.get("vulns")

    def get_vulnerabilities(self) -> list:
        """Returns a filtred list of Vulnerabilities

        returns:
            id,
            description,
            affected_versions,
            fixed_version
        """

        reports = [reports for reports in self.data]

        return [
            {
                "id": r["id"],
                "description": r["details"],
                "affected_versions": r["affected"].get("versions"),
                "fixed_version": r["affected"].get("ranges"),
            }
            for r in reports
        ]

    def get_blacklisted_versions(self) -> list:
        """Returns a list of problematic versions"""

        reports = [reports for reports in self.data]
        not_flatten_list = [r["affected"].get("versions") for r in reports]

        return [item for sub_list in not_flatten_list for item in sub_list]
