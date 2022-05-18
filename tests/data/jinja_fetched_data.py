EXPECTED_VULNERABILITIES = [
    {
        "id": "PYSEC-2014-8",
        "description": "The default configuration for bccache.FileSystemBytecodeCache in Jinja2 before 2.7.2 does not properly create temporary files, which allows local users to gain privileges via a crafted .cache file with a name starting with __jinja2_ in /tmp.",
        "affected": [
            {
                "package": {
                    "name": "jinja2",
                    "ecosystem": "PyPI",
                    "purl": "pkg:pypi/jinja2",
                },
                "ranges": [
                    {
                        "type": "ECOSYSTEM",
                        "events": [{"introduced": "0"}, {"fixed": "2.7.2"}],
                    }
                ],
                "versions": [
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
                ],
                "database_specific": {
                    "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2014-8.yaml"
                },
            }
        ],
    },
    {
        "id": "PYSEC-2014-82",
        "description": "FileSystemBytecodeCache in Jinja2 2.7.2 does not properly create temporary directories, which allows local users to gain privileges by pre-creating a temporary directory with a user's uid.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2014-1402.",
        "affected": [
            {
                "package": {
                    "name": "jinja2",
                    "ecosystem": "PyPI",
                    "purl": "pkg:pypi/jinja2",
                },
                "ranges": [
                    {
                        "type": "GIT",
                        "repo": "https://github.com/mitsuhiko/jinja2",
                        "events": [
                            {"introduced": "0"},
                            {"fixed": "acb672b6a179567632e032f547582f30fa2f4aa7"},
                        ],
                    },
                    {
                        "type": "ECOSYSTEM",
                        "events": [{"introduced": "0"}, {"fixed": "2.7.3"}],
                    },
                ],
                "versions": [
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
                    "2.7.2",
                ],
                "database_specific": {
                    "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2014-82.yaml"
                },
            }
        ],
    },
    {
        "id": "PYSEC-2019-217",
        "description": "In Pallets Jinja before 2.10.1, str.format_map allows a sandbox escape.",
        "affected": [
            {
                "package": {
                    "name": "jinja2",
                    "ecosystem": "PyPI",
                    "purl": "pkg:pypi/jinja2",
                },
                "ranges": [
                    {
                        "type": "ECOSYSTEM",
                        "events": [{"introduced": "0"}, {"fixed": "2.10.1"}],
                    }
                ],
                "versions": [
                    "2.0",
                    "2.0rc1",
                    "2.1",
                    "2.1.1",
                    "2.10",
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
                    "2.7.2",
                    "2.7.3",
                    "2.8",
                    "2.8.1",
                    "2.9",
                    "2.9.1",
                    "2.9.2",
                    "2.9.3",
                    "2.9.4",
                    "2.9.5",
                    "2.9.6",
                ],
                "database_specific": {
                    "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2019-217.yaml"
                },
            }
        ],
    },
    {
        "id": "PYSEC-2019-220",
        "description": "In Pallets Jinja before 2.8.1,str.format allows a sandbox escape.",
        "affected": [
            {
                "package": {
                    "name": "jinja2",
                    "ecosystem": "PyPI",
                    "purl": "pkg:pypi/jinja2",
                },
                "ranges": [
                    {
                        "type": "GIT",
                        "repo": "https://github.com/pallets/jinja",
                        "events": [
                            {"introduced": "0"},
                            {"fixed": "9b53045c34e61013dc8f09b7e52a555fa16bed16"},
                        ],
                    },
                    {
                        "type": "ECOSYSTEM",
                        "events": [{"introduced": "0"}, {"fixed": "2.8.1"}],
                    },
                ],
                "versions": [
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
                    "2.7.2",
                    "2.7.3",
                    "2.8",
                ],
                "database_specific": {
                    "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2019-220.yaml"
                },
            }
        ],
    },
    {
        "id": "PYSEC-2021-66",
        "description": "This affects the package jinja2 from 0.0.0 and before 2.11.3. The ReDoS vulnerability is mainly due to the `_punctuation_re regex` operator and its use of multiple wildcards. The last wildcard is the most exploitable as it searches for trailing punctuation. This issue can be mitigated by Markdown to format user content instead of the urlize filter, or by implementing request timeouts and limiting process memory.",
        "affected": [
            {
                "package": {
                    "name": "jinja2",
                    "ecosystem": "PyPI",
                    "purl": "pkg:pypi/jinja2",
                },
                "ranges": [
                    {
                        "type": "ECOSYSTEM",
                        "events": [{"introduced": "0"}, {"fixed": "2.11.3"}],
                    }
                ],
                "versions": [
                    "2.0rc1",
                    "2.0",
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
                    "2.7.2",
                    "2.7.3",
                    "2.8",
                    "2.8.1",
                    "2.9",
                    "2.9.1",
                    "2.9.2",
                    "2.9.3",
                    "2.9.4",
                    "2.9.5",
                    "2.9.6",
                    "2.10",
                    "2.10.1",
                    "2.10.2",
                    "2.10.3",
                    "2.11.0",
                    "2.11.1",
                    "2.11.2",
                ],
                "database_specific": {
                    "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2021-66.yaml"
                },
            }
        ],
    },
]

BLACKLISTED_VERSIONS = [
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
    "2.7.2",
    "2.0",
    "2.0rc1",
    "2.1",
    "2.1.1",
    "2.10",
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
    "2.7.2",
    "2.7.3",
    "2.8",
    "2.8.1",
    "2.9",
    "2.9.1",
    "2.9.2",
    "2.9.3",
    "2.9.4",
    "2.9.5",
    "2.9.6",
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
    "2.7.2",
    "2.7.3",
    "2.8",
    "2.0rc1",
    "2.0",
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
    "2.7.2",
    "2.7.3",
    "2.8",
    "2.8.1",
    "2.9",
    "2.9.1",
    "2.9.2",
    "2.9.3",
    "2.9.4",
    "2.9.5",
    "2.9.6",
    "2.10",
    "2.10.1",
    "2.10.2",
    "2.10.3",
    "2.11.0",
    "2.11.1",
    "2.11.2",
]

RAW_DATA = {
    "vulns": [
        {
            "id": "PYSEC-2014-8",
            "details": "The default configuration for bccache.FileSystemBytecodeCache in Jinja2 before 2.7.2 does not properly create temporary files, which allows local users to gain privileges via a crafted .cache file with a name starting with __jinja2_ in /tmp.",
            "aliases": ["CVE-2014-1402"],
            "modified": "2021-07-05T00:01:22.043149Z",
            "published": "2014-05-19T14:55:00Z",
            "references": [
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
            ],
            "affected": [
                {
                    "package": {
                        "name": "jinja2",
                        "ecosystem": "PyPI",
                        "purl": "pkg:pypi/jinja2",
                    },
                    "ranges": [
                        {
                            "type": "ECOSYSTEM",
                            "events": [{"introduced": "0"}, {"fixed": "2.7.2"}],
                        }
                    ],
                    "versions": [
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
                    ],
                    "database_specific": {
                        "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2014-8.yaml"
                    },
                }
            ],
            "schema_version": "1.2.0",
        },
        {
            "id": "PYSEC-2014-82",
            "details": "FileSystemBytecodeCache in Jinja2 2.7.2 does not properly create temporary directories, which allows local users to gain privileges by pre-creating a temporary directory with a user's uid.  NOTE: this vulnerability exists because of an incomplete fix for CVE-2014-1402.",
            "aliases": ["CVE-2014-0012"],
            "modified": "2021-08-27T03:22:05.027573Z",
            "published": "2014-05-19T14:55:00Z",
            "references": [
                {
                    "type": "REPORT",
                    "url": "https://bugzilla.redhat.com/show_bug.cgi?id=1051421",
                },
                {"type": "WEB", "url": "https://github.com/mitsuhiko/jinja2/pull/292"},
                {
                    "type": "FIX",
                    "url": "https://github.com/mitsuhiko/jinja2/commit/acb672b6a179567632e032f547582f30fa2f4aa7",
                },
                {"type": "WEB", "url": "http://seclists.org/oss-sec/2014/q1/73"},
                {"type": "WEB", "url": "https://github.com/mitsuhiko/jinja2/pull/296"},
                {"type": "ADVISORY", "url": "http://secunia.com/advisories/60738"},
                {
                    "type": "WEB",
                    "url": "http://www.gentoo.org/security/en/glsa/glsa-201408-13.xml",
                },
                {"type": "ADVISORY", "url": "http://secunia.com/advisories/56328"},
            ],
            "affected": [
                {
                    "package": {
                        "name": "jinja2",
                        "ecosystem": "PyPI",
                        "purl": "pkg:pypi/jinja2",
                    },
                    "ranges": [
                        {
                            "type": "GIT",
                            "repo": "https://github.com/mitsuhiko/jinja2",
                            "events": [
                                {"introduced": "0"},
                                {"fixed": "acb672b6a179567632e032f547582f30fa2f4aa7"},
                            ],
                        },
                        {
                            "type": "ECOSYSTEM",
                            "events": [{"introduced": "0"}, {"fixed": "2.7.3"}],
                        },
                    ],
                    "versions": [
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
                        "2.7.2",
                    ],
                    "database_specific": {
                        "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2014-82.yaml"
                    },
                }
            ],
            "schema_version": "1.2.0",
        },
        {
            "id": "PYSEC-2019-217",
            "details": "In Pallets Jinja before 2.10.1, str.format_map allows a sandbox escape.",
            "aliases": ["CVE-2019-10906", "GHSA-462w-v97r-4m45"],
            "modified": "2021-11-22T04:57:52.862665Z",
            "published": "2019-04-07T00:29:00Z",
            "references": [
                {
                    "type": "ARTICLE",
                    "url": "https://palletsprojects.com/blog/jinja-2-10-1-released",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/b2380d147b508bbcb90d2cad443c159e63e12555966ab4f320ee22da@%3Ccommits.airflow.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/46c055e173b52d599c648a98199972dbd6a89d2b4c4647b0500f2284@%3Cdevnull.infra.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/f0c4a03418bcfe70c539c5dbaf99c04c98da13bfa1d3266f08564316@%3Ccommits.airflow.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/7f39f01392d320dfb48e4901db68daeece62fd60ef20955966739993@%3Ccommits.airflow.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/57673a78c4d5c870d3f21465c7e2946b9f8285c7c57e54c2ae552f02@%3Ccommits.airflow.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/320441dccbd9a545320f5f07306d711d4bbd31ba43dc9eebcfc602df@%3Cdevnull.infra.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/2b52b9c8b9d6366a4f1b407a8bde6af28d9fc73fdb3b37695fd0d9ac@%3Cdevnull.infra.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.apache.org/thread.html/09fc842ff444cd43d9d4c510756fec625ef8eb1175f14fd21de2605f@%3Cdevnull.infra.apache.org%3E",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/QCDYIS254EJMBNWOG4S5QY6AOTOR4TZU/",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/DSW3QZMFVVR7YE3UT4YRQA272TYAL5AF/",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/TS7IVZAJBWOHNRDMFJDIZVFCMRP6YIUQ/",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:1152",
                },
                {
                    "type": "WEB",
                    "url": "http://lists.opensuse.org/opensuse-security-announce/2019-05/msg00030.html",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:1237",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:1329",
                },
                {"type": "WEB", "url": "https://usn.ubuntu.com/4011-1/"},
                {"type": "WEB", "url": "https://usn.ubuntu.com/4011-2/"},
                {
                    "type": "WEB",
                    "url": "http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00064.html",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://github.com/advisories/GHSA-462w-v97r-4m45",
                },
            ],
            "affected": [
                {
                    "package": {
                        "name": "jinja2",
                        "ecosystem": "PyPI",
                        "purl": "pkg:pypi/jinja2",
                    },
                    "ranges": [
                        {
                            "type": "ECOSYSTEM",
                            "events": [{"introduced": "0"}, {"fixed": "2.10.1"}],
                        }
                    ],
                    "versions": [
                        "2.0",
                        "2.0rc1",
                        "2.1",
                        "2.1.1",
                        "2.10",
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
                        "2.7.2",
                        "2.7.3",
                        "2.8",
                        "2.8.1",
                        "2.9",
                        "2.9.1",
                        "2.9.2",
                        "2.9.3",
                        "2.9.4",
                        "2.9.5",
                        "2.9.6",
                    ],
                    "database_specific": {
                        "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2019-217.yaml"
                    },
                }
            ],
            "schema_version": "1.2.0",
        },
        {
            "id": "PYSEC-2019-220",
            "details": "In Pallets Jinja before 2.8.1,str.format allows a sandbox escape.",
            "aliases": ["CVE-2016-10745", "GHSA-hj2j-77xm-mc5v"],
            "modified": "2021-11-22T04:57:52.929678Z",
            "published": "2019-04-08T13:29:00Z",
            "references": [
                {
                    "type": "ARTICLE",
                    "url": "https://palletsprojects.com/blog/jinja-281-released/",
                },
                {
                    "type": "FIX",
                    "url": "https://github.com/pallets/jinja/commit/9b53045c34e61013dc8f09b7e52a555fa16bed16",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:1022",
                },
                {
                    "type": "WEB",
                    "url": "http://lists.opensuse.org/opensuse-security-announce/2019-05/msg00030.html",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:1237",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:1260",
                },
                {"type": "WEB", "url": "https://usn.ubuntu.com/4011-1/"},
                {"type": "WEB", "url": "https://usn.ubuntu.com/4011-2/"},
                {
                    "type": "WEB",
                    "url": "http://lists.opensuse.org/opensuse-security-announce/2019-06/msg00064.html",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:3964",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://access.redhat.com/errata/RHSA-2019:4062",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://github.com/advisories/GHSA-hj2j-77xm-mc5v",
                },
            ],
            "affected": [
                {
                    "package": {
                        "name": "jinja2",
                        "ecosystem": "PyPI",
                        "purl": "pkg:pypi/jinja2",
                    },
                    "ranges": [
                        {
                            "type": "GIT",
                            "repo": "https://github.com/pallets/jinja",
                            "events": [
                                {"introduced": "0"},
                                {"fixed": "9b53045c34e61013dc8f09b7e52a555fa16bed16"},
                            ],
                        },
                        {
                            "type": "ECOSYSTEM",
                            "events": [{"introduced": "0"}, {"fixed": "2.8.1"}],
                        },
                    ],
                    "versions": [
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
                        "2.7.2",
                        "2.7.3",
                        "2.8",
                    ],
                    "database_specific": {
                        "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2019-220.yaml"
                    },
                }
            ],
            "schema_version": "1.2.0",
        },
        {
            "id": "PYSEC-2021-66",
            "details": "This affects the package jinja2 from 0.0.0 and before 2.11.3. The ReDoS vulnerability is mainly due to the `_punctuation_re regex` operator and its use of multiple wildcards. The last wildcard is the most exploitable as it searches for trailing punctuation. This issue can be mitigated by Markdown to format user content instead of the urlize filter, or by implementing request timeouts and limiting process memory.",
            "aliases": [
                "CVE-2020-28493",
                "SNYK-PYTHON-JINJA2-1012994",
                "GHSA-g3rq-g295-4j3m",
            ],
            "modified": "2021-03-22T16:34:00Z",
            "published": "2021-02-01T20:15:00Z",
            "references": [
                {
                    "type": "WEB",
                    "url": "https://github.com/pallets/jinja/blob/ab81fd9c277900c85da0c322a2ff9d68a235b2e6/src/jinja2/utils.py%23L20",
                },
                {"type": "WEB", "url": "https://github.com/pallets/jinja/pull/1343"},
                {
                    "type": "ADVISORY",
                    "url": "https://snyk.io/vuln/SNYK-PYTHON-JINJA2-1012994",
                },
                {
                    "type": "WEB",
                    "url": "https://lists.fedoraproject.org/archives/list/package-announce@lists.fedoraproject.org/message/PVAKCOO7VBVUBM3Q6CBBTPBFNP5NDXF4/",
                },
                {
                    "type": "ADVISORY",
                    "url": "https://github.com/advisories/GHSA-g3rq-g295-4j3m",
                },
            ],
            "affected": [
                {
                    "package": {
                        "name": "jinja2",
                        "ecosystem": "PyPI",
                        "purl": "pkg:pypi/jinja2",
                    },
                    "ranges": [
                        {
                            "type": "ECOSYSTEM",
                            "events": [{"introduced": "0"}, {"fixed": "2.11.3"}],
                        }
                    ],
                    "versions": [
                        "2.0rc1",
                        "2.0",
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
                        "2.7.2",
                        "2.7.3",
                        "2.8",
                        "2.8.1",
                        "2.9",
                        "2.9.1",
                        "2.9.2",
                        "2.9.3",
                        "2.9.4",
                        "2.9.5",
                        "2.9.6",
                        "2.10",
                        "2.10.1",
                        "2.10.2",
                        "2.10.3",
                        "2.11.0",
                        "2.11.1",
                        "2.11.2",
                    ],
                    "database_specific": {
                        "source": "https://github.com/pypa/advisory-database/blob/main/vulns/jinja2/PYSEC-2021-66.yaml"
                    },
                }
            ],
            "schema_version": "1.2.0",
        },
    ]
}
