import pkg_resources as pkg_info

from version import VERSION


def test_version():
    assert VERSION == pkg_info.get_distribution("pre-audit").version
