"""Check what is printed on terminal"""

from unittest import mock
import pytest
from click.testing import CliRunner

from src.commands.cli import audit_package

# Exceptions
from requests.exceptions import HTTPError, Timeout, ConnectionError
from src.core.utils.exceptions import PackageNotFound


class TestEcho:
    """Test if commands and options is returning all alright"""

    def test_package_audit_command(self):
        """Test: `pre-audit <package> <version>`"""

        runner = CliRunner()
        result = runner.invoke(audit_package, ["Django", "3.2"])

        assert result.exit_code == 0
        assert not result.exception
        assert "Vulnerabilities founded!" in result.output
        assert "GHSA-" in result.output

    def test_all_affected_versions_command(self):
        """Test: `pre-audit <package> <version> --affected`"""

        runner = CliRunner()
        result = runner.invoke(audit_package, ["Django", "3.2", "--affected"])

        assert result.exit_code == 0
        assert not result.exception
        assert "Affected versions" in result.output
        assert "." in result.output


class TestAuditExepcions:
    """Test if is printing alright when raises an Exception"""

    @mock.patch("src.commands.cli.audit_core.run", side_effect=PackageNotFound())
    def test_package_not_found_exception(self, mock_run_audit):
        """Check for `PackageNotFound`"""

        with pytest.raises(PackageNotFound) as err:
            runner = CliRunner()
            result = runner.invoke(audit_package, ["Django", "3.2"])
            mock_run_audit()
        assert "Package isn't in OSV's DataBase!" in result.output

    @mock.patch("src.commands.cli.audit_core.run", side_effect=HTTPError())
    def test_http_error_exeption(self, mock_run_audit):
        """Check for `HTTPError`"""

        with pytest.raises(HTTPError) as err:
            runner = CliRunner()
            result = runner.invoke(audit_package, ["Django", "3.2"])
            mock_run_audit()
        assert "Http Error:" in result.output

    @mock.patch("src.commands.cli.audit_core.run", side_effect=ConnectionError())
    def test_connection_error_exeption(self, mock_run_audit):
        """Check for `ConnectionError`"""

        with pytest.raises(ConnectionError) as err:
            runner = CliRunner()
            result = runner.invoke(audit_package, ["Django", "3.2"])
            mock_run_audit()
        assert "Connection Error!" in result.output

    @mock.patch("src.commands.cli.audit_core.run", side_effect=Timeout())
    def test_timeout_exeption(self, mock_run_audit):
        """Check for `Timeout`"""

        with pytest.raises(Timeout) as err:
            runner = CliRunner()
            result = runner.invoke(audit_package, ["Django", "3.2"])
            mock_run_audit()
        assert "Request Timeout!" in result.output
