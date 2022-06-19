"""This is the entry of terminal commands"""

import click
from requests.exceptions import HTTPError, Timeout, ConnectionError

from src.commands.ux.message_type import warn
from src.commands.core import audit_core

from src.core.utils.exceptions import PackageNotFound


@click.command(name="package")
@click.argument("package")
@click.argument("version")
@click.option("--affected", is_flag=True)
def audit_package(package, version, affected):
    """Fetches in OSV for vulnerabilities"""

    has_all_affected_option = affected

    try:
        audit_core.run(package, version, has_all_affected_option)

    except PackageNotFound:
        warn("Package isn't in OSV's DataBase!\n")
    except HTTPError as err:
        warn("Http Error: {}\n".format(err))
    except ConnectionError as err:
        warn("Connection Error!\n".format(err))
    except Timeout:
        warn("Request Timeout! :(\n")
