import pytest

from core.fetch_api import OsvApi
from core.utils.exceptions import PackageNotFound


@pytest.fixture
def django_2_pkg():
    return OsvApi("Django", "2.0").fetch()


@pytest.fixture
def fake_pkg():
    return OsvApi("FakePackageThatDoesNotExists", "10.2@fake")


def test_real_pkg_found(django_2_pkg):
    assert django_2_pkg != {}


def test_fake_pkg(fake_pkg):
    try:
        fake_pkg.fetch()
        assert False
    # always will fail
    except:
        assert True
