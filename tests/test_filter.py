import pytest

from core.filter import FilterForOsvVulns
from data.jinja_fetched_data import (
    BLACKLISTED_VERSIONS,
    EXPECTED_VULNERABILITIES,
    RAW_DATA,
)


def test_get_vulnerabilities():
    expected = EXPECTED_VULNERABILITIES
    model = FilterForOsvVulns(RAW_DATA)
    assert model.get_vulnerabilities() == expected


def test_affected_versions():
    expected = BLACKLISTED_VERSIONS
    model = FilterForOsvVulns(RAW_DATA)
    assert model.get_blacklisted_versions() == expected
