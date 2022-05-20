from pytest import fixture

from data.jinja_fetched_data import RAW_DATA

from core.filter_report import FilterByReport


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


def test_get_references():
    references = [
        {
            "type": "WEB",
            "url": "https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=734747",
        },
        {
            "type": "ADVISORY",
            "url": "http://advisories.mageia.org/MGASA-2014-0028.html",
        },
        {"type": "WEB", "url": "http://jinja.pocoo.org/docs/changelog/"},
        {
            "type": "WEB",
            "url": "http://openwall.com/lists/oss-security/2014/01/10/3",
        },
        {
            "type": "REPORT",
            "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1051421",
        },
        {
            "type": "ADVISORY",
            "url": "http://www.mandriva.com/security/advisories?name=MDVSA-2014:096",
        },
        {
            "type": "WEB",
            "url": "http://openwall.com/lists/oss-security/2014/01/10/2",
        },
        {"type": "ADVISORY", "url": "http://secunia.com/advisories/59017"},
        {"type": "ADVISORY", "url": "http://secunia.com/advisories/58918"},
        {"type": "ADVISORY", "url": "http://secunia.com/advisories/60770"},
        {"type": "ADVISORY", "url": "http://secunia.com/advisories/60738"},
        {"type": "ADVISORY", "url": "http://secunia.com/advisories/56287"},
        {
            "type": "WEB",
            "url": "http://www.gentoo.org/security/en/glsa/glsa-201408-13.xml",
        },
        {
            "type": "WEB",
            "url": "https://oss.oracle.com/pipermail/el-errata/2014-June/004192.html",
        },
        {"type": "ADVISORY", "url": "http://secunia.com/advisories/58783"},
        {
            "type": "ADVISORY",
            "url": "http://rhn.redhat.com/errata/RHSA-2014-0748.html",
        },
        {
            "type": "ADVISORY",
            "url": "http://rhn.redhat.com/errata/RHSA-2014-0747.html",
        },
    ]
    assert FilterByReport.get_references(entry) == references
