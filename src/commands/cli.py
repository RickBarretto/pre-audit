"""This is the entry of terminal commands"""

import click
from requests.exceptions import HTTPError, Timeout, ConnectionError

from src.core.fetch_api import OsvApi
from src.core.filter_report import Filter
from src.core.utils.osv_model import OsvModel
from src.core.utils.exceptions import PackageNotFound


@click.command(name="package")
@click.argument("package")
@click.argument("version")
def audit_package(package, version):
    """Fetches in OSV for vulnerabilities"""

    pkg = OsvModel(package, version)

    try:
        data = OsvApi(pkg).fetch()

        f = Filter(data)
        click.secho("Vulnerabilities founded!\n", fg="red", bold=True)
        info = f.get_main_info()

        for i in info:
            click.secho("{}: ".format(i[0]), fg="red", bold=True)
            click.secho("{}\n".format(i[1]), fg="blue")
    except PackageNotFound:
        click.secho("Package isn't in OSV's DataBase!\n", fg="red", bold=True)
    except HTTPError as err:
        click.secho("Http Error: {}\n".format(err), fg="red", bold=True)
    except ConnectionError:
        click.secho("Connection Error!\n".format(err), fg="red", bold=True)
    except Timeout:
        click.secho("Request Timeout! :(\n", fg="red", bold=True)
