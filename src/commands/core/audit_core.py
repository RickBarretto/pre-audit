"""Low level of audit command"""

from src.commands.ux import audit_command_ui
from src.core.fetch_api import OsvApi
from src.core.filter_report import Filter

__all__ = ["run"]


class _Utils:
    @staticmethod
    def fetch(package: str, version: str) -> list:
        """Fetches the data from OsvApi"""
        return Filter(OsvApi(package, version).fetch())

    @staticmethod
    def get_main_info(filtred_data: Filter) -> list:
        """Get the main info to print"""
        return filtred_data.get_main_info()

    @staticmethod
    def get_all_affected_versions_info(filtred_data: Filter) -> list:
        """Gets all affected version"""
        return filtred_data.get_all_affected_versions()


def run(package: str, version: str, has_all_affected_option: bool):
    """Empower the audit command"""

    data = _Utils.fetch(package, version)

    if has_all_affected_option:
        affected = _Utils.get_all_affected_versions_info(data)
        audit_command_ui.echo_affected(affected)

    else:
        info = _Utils.get_main_info(data)
        audit_command_ui.echo_main(info)
