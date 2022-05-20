from src.core.utils.flatten_list import flatten_list


class AllAffectedVersions:
    @staticmethod
    def _affected_dict(reports) -> dict:
        return [report["affected"] for report in reports]

    @staticmethod
    def get(reports) -> list:
        affected_reports = AllAffectedVersions._affected_dict(reports)
        not_flatten = [a["versions"] for sublist in affected_reports for a in sublist]
        return flatten_list(not_flatten)
