from click.testing import CliRunner
from src.commands.cli import audit_package


def test_package_audit():
    runner = CliRunner()
    result = runner.invoke(audit_package, ["Django", "3.2"])
    assert result.exit_code == 0
    assert not result.exception
    assert "Vulnerabilities founded!" in result.output
    assert "GHSA-" in result.output
