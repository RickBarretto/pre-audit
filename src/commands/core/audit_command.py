"""Low level of audit command"""

from src.commands.core import get_package_info
from src.commands.ux import audit_command_ui


def run(package: str, version: str, has_all_affected_option: bool):
    """Empower the audit command"""

    data = get_package_info.fetch(package, version)

    if has_all_affected_option:
        affected = get_package_info.get_all_affected_versions_info(data)
        audit_command_ui.echo_affected(affected)

    else:
        info = get_package_info.get_main_info(data)
        audit_command_ui.echo_main(info)
