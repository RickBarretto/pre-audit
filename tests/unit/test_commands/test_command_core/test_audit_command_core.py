import pytest
from unittest import mock
from click.testing import CliRunner

from src.commands.core.audit_core import _Utils, run, Filter


class TestUtils:
    @mock.patch("src.commands.core.audit_core.OsvApi.fetch")
    def test_fetch(self, mock_osv):
        """Checks if Filter is returning values inside 'vulns'"""

        mock_osv.return_value = {
            "vulns": [{"id": "GHA-xxxx-xxxx"}, {"id": "GHA-yyyy-yyyy"}]
        }

        filter_obj = _Utils.fetch("FakePkg", "f3.2")
        entry = filter_obj.reports
        expected = [{"id": "GHA-xxxx-xxxx"}, {"id": "GHA-yyyy-yyyy"}]

        assert entry == expected
