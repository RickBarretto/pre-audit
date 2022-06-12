"""Low level of audit command"""

from src.commands.core import get_package_info
from src.commands.ux import audit_command_ui


def run(package: str, version: str, has_all_affected_option: bool):
    """Empower the audit command"""

    data = get_package_info.fetch(package, version)
    info = get_package_info.get_main_info(data)

    audit_command.echo_main(info)

    if has_all_affected_option:
        affected = get_package_info.get_all_affected_versions_info(data)
        audit_command.echo_affected(affected)