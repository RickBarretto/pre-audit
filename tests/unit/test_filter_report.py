import pytest

from data.jinja_fetched_data import RAW_DATA, BLACKLISTED_VERSIONS

from core.filter_report import Filter

filter_class = Filter(RAW_DATA)
index = 0


def test_get_id():
    assert filter_class.get_id(index) == "PYSEC-2014-8"


def test_get_description():
    description = "The default configuration for bccache.FileSystemBytecodeCache in Jinja2 before 2.7.2 does not properly create temporary files, which allows local users to gain privileges via a crafted .cache file with a name starting with __jinja2_ in /tmp."
    assert filter_class.get_description(index) == description


def test_get_aliases():
    assert filter_class.get_aliases(index) == ["CVE-2014-1402"]


def test_get_affected_versions():
    versions = BLACKLISTED_VERSIONS
    assert filter_class.get_all_affected_versions() == versions


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
    assert filter_class.get_references(index) == references
