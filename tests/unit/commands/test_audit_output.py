from click.testing import CliRunner
from pytest_print import printer

from src.commands.cli import audit_package


def test_package_audit_command():
    runner = CliRunner()
    result = runner.invoke(audit_package, ["Django", "3.2"])

    assert result.exit_code == 0
    assert not result.exception
    assert "Vulnerabilities founded!" in result.output
    assert "GHSA-" in result.output


def test_all_affected_versions_command(printer):
    runner = CliRunner()
    result = runner.invoke(audit_package, ["Django", "3.2", "--affected"])

    assert result.exit_code == 0
    assert not result.exception
    assert "Affected versions" in result.output
    assert "." in result.output
