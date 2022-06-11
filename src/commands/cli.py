"""This is the entry of terminal commands"""

import click
from requests.exceptions import HTTPError, Timeout, ConnectionError

from src.commands.ux import message_type
from src.commands.core.get_package_info import get_package_info

from src.core.utils.exceptions import PackageNotFound


@click.command(name="package")
@click.argument("package")
@click.argument("version")
def audit_package(package, version):
    """Fetches in OSV for vulnerabilities"""

    try:
        info = get_package_info(package, version)
        message_type.warn("Vulnerabilities founded!\n")
        for i in info:
            message_type.warn("{}: ".format(i[0]))
            message_type.info("{}\n".format(i[1]))

    except PackageNotFound:
        message_type.warn("Package isn't in OSV's DataBase!\n")
    except HTTPError as err:
        message_type.warn("Http Error: {}\n".format(err))
    except ConnectionError as err:
        message_type.warn("Connection Error!\n".format(err))
    except Timeout:
        message_type.warn("Request Timeout! :(\n")
