"""This is the entry of terminal commands"""

import click
from requests.exceptions import HTTPError, Timeout, ConnectionError

from src.commands.ux import message_type
from src.commands.core import audit_command

from src.core.utils.exceptions import PackageNotFound


@click.command(name="package")
@click.argument("package")
@click.argument("version")
@click.option("--affected", is_flag=True)
def audit_package(package, version, affected):
    """Fetches in OSV for vulnerabilities"""

    has_all_affected_option = affected

    try:
        audit_command.run(package, version, has_all_affected_option)

    except PackageNotFound:
        message_type.warn("Package isn't in OSV's DataBase!\n")
    except HTTPError as err:
        message_type.warn("Http Error: {}\n".format(err))
    except ConnectionError as err:
        message_type.warn("Connection Error!\n".format(err))
    except Timeout:
        message_type.warn("Request Timeout! :(\n")
