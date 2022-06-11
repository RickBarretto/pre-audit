"""This is the entry of terminal commands"""

import click
from requests.exceptions import HTTPError, Timeout, ConnectionError

from src.commands.ux import message_type

from src.core.fetch_api import OsvApi
from src.core.filter_report import Filter
from src.core.utils.exceptions import PackageNotFound


@click.command(name="package")
@click.argument("package")
@click.argument("version")
def audit_package(package, version):
    """Fetches in OSV for vulnerabilities"""

    try:
        data = OsvApi(package, version).fetch()

        f = Filter(data)
        message_type.warn("Vulnerabilities founded!\n")
        info = f.get_main_info()

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
