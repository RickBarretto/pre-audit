from pytest import fixture

from data.jinja_fetched_data import RAW_DATA

from models.filter_report import FilterByReport


data = RAW_DATA
reports = data.get("vulns")
entry = reports[0]


def test_get_id():
    assert FilterByReport.get_id(entry) == "PYSEC-2014-8"


def test_get_description():
    description = "The default configuration for bccache.FileSystemBytecodeCache in Jinja2 before 2.7.2 does not properly create temporary files, which allows local users to gain privileges via a crafted .cache file with a name starting with __jinja2_ in /tmp."
    assert FilterByReport.get_description(entry) == description


def test_get_aliases():
    assert FilterByReport.get_aliases(entry) == ["CVE-2014-1402"]


def test_get_affected_versions():
    versions = [
        "2.0",
        "2.0rc1",
        "2.1",
        "2.1.1",
        "2.2",
        "2.2.1",
        "2.3",
        "2.3.1",
        "2.4",
        "2.4.1",
        "2.5",
        "2.5.1",
        "2.5.2",
        "2.5.3",
        "2.5.4",
        "2.5.5",
        "2.6",
        "2.7",
        "2.7.1",
    ]
    assert FilterByReport.get_affected_versions(entry) == versions
