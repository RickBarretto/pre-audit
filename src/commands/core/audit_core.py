"""Low level of audit command"""

from src.core.fetch_api import OsvApi
from src.core.filter_report import Filter

__all__ = ["run"]


class _Utils:
    @staticmethod
    def fetch(package: str, version: str) -> list:
        """Fetches the data from OsvApi"""
        return Filter(OsvApi(package, version).fetch())


class Ux:
    @staticmethod
    def echo_main(info: list):
        message_type.warn("Vulnerabilities founded!\n")
        for i in info:
            message_type.warn("{}: ".format(i[0]))
            message_type.info("{}\n".format(i[1]))

    @staticmethod
    def echo_affected(info: list):
        message_type.warn("Affected versions")
        for i in info:
            message_type.info(i)


def run(package: str, version: str, has_all_affected_option: bool):
    """Empower the audit command"""

    data = _Utils.fetch(package, version)

    if has_all_affected_option:
        affected = data.get_all_affected_versions()
        Ux.echo_affected(affected)

    else:
        info = data.get_main_info()
        Ux.echo_main(info)
