import click


@click.command(name="package")
@click.argument("package")
@click.argument("version")
def audit_package(package, version):
    reports = fetch(package, version)
    Standard(reports)
