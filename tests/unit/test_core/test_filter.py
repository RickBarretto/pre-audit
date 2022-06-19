"""Test Filter

- `core.filter_report`
"""

import pytest

from core.filter_report import Filter


@pytest.fixture(scope="module")
def index() -> int:
    return 0


@pytest.mark.usefixtures("django_filter")
class TestDjangoFilter:
    """Test Filter's methods
    with real fetched data stored locally
    """

    def test_get_main(self, django_filter, expected_main):
        assert django_filter.get_main_info() == expected_main

    def test_get_affected_data(self, django_filter, expected_affected_versions):
        assert django_filter.get_all_affected_versions() == expected_affected_versions

    def test_get_id(self, django_filter, expected_id, index):
        assert django_filter.get_id(index) == expected_id

    def test_get_description(self, django_filter, expected_description, index):
        assert django_filter.get_description(index) == expected_description

    def test_get_aliases(self, django_filter, expected_aliases, index):
        assert django_filter.get_aliases(index) == expected_aliases

    def test_get_references(self, django_filter, expected_references, index):
        assert django_filter.get_references(index) == expected_references
