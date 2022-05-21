"""This is the entry of terminal commands"""

import click

from src.core.fetch_api import fetch_api
from src.core.filter_report import Filter
from src.core.utils.osv_model import OsvModel


@click.command(name="package")
@click.argument("package")
@click.argument("version")
def audit_package(package, version):
    """Fetches in OSV for vulnerabilities"""

    data = fetch_api(OsvModel(package, version))
    f = Filter(data)
    click.secho("Vulnerabilities founded!\n", fg="red", bold=True)
    info = f.get_main_info()

    for i in info:
        click.secho("{}: ".format(i[0]), fg="red", bold=True)
        click.secho("{}\n".format(i[1]), fg="blue")
