# pre-audit

[![Python package](https://github.com/RickBarretto/pre-audit/actions/workflows/main.yml/badge.svg)](https://github.com/RickBarretto/pre-audit/actions/workflows/main.yml)

> pre-audit is a application that tries to resolve some
securit problems. Nothing too special, getting real...

pre-audit just fetches the [OSV's api](https://osv.dev/list?ecosystem=PyPI)
that is a big database of Vulnerabilities and supports the PyPI Ecossystem.

## What pre-audit isn't is
- A source code auditor (use [Bandit](https://github.com/PyCQA/bandit)
    or [Snyk IDE-Plugins](https://snyk.io/ide-plugins/), instead)
- An antivirus
- A package manager
    [(Recommend to use Poetry, in this case)](https://python-poetry.org/)

## Why this project

Other projects just analyzes vulnerabilities after download the packages,
what is a big problem for Supply Chain Security.

Typosquatting and `sdist`s are great problems for this.

- Typosquatting is growing as a form of Supply Chain attack,
    search for a famous package and you'll have a lot of packages
    with similar names
- `sdist`s are a big problem too, it can execute arbitrary code. (thank you, `setup.py`!)

> "You are not just installing malware,
you are running it from the moment you run pip install,
thanks to sdist packages' ability to run arbitrary code.
This kind of attack is called typosquatting,
and has happened many times in PyPI"
> - [Carles Garcia](https://carles-garcia.net/python/python_pip/)

Links for Supply Chain in Python:
- [The security risks of pip and PyPI - Carles Garcia-Cabot](https://carles-garcia.net/python/python_pip/)
- [Arbitrary Code Execution During Python Package Installation - Andrew Scott at Ochrona Security](https://medium.com/ochrona/arbitrary-code-execution-during-python-package-installation-3a60990350ef)
- [PyPI Security Pitfalls And Steps Towards A Secure Python Ecosystem - Dana Crane at ActiveState](https://www.activestate.com/blog/pypi-security-pitfalls-and-steps-towards-a-secure-python-ecosystem/)

## Install

```shell
$ poetry add git+https://github.com/RickBarretto/pre-audit.git
```

## Usage

```shell
$ pre-audit Django 3.0
Vulnerabilities founded!

GHSA-fvgf-6h6h-3322:
In Django 2.2 before 2.2.18, 3.0 before 3.0.12, and 3.1 before 3.1.6, the django.utils.archive.extract method (used by "startapp --template" and "startproject --template") allows directory traversal via an archive with absolute paths or relative paths with dot segments.

GHSA-rxjp-mfm9-w4wr:
In Django 2.2 before 2.2.21, 3.1 before 3.1.9, and 3.2 before 3.2.1, MultiPartParser, UploadedFile, and FieldFile allowed directory traversal via uploaded files with suitably crafted file names.

GHSA-v6rh-hp5x-86rv:
In Django 2.2 before 2.2.25, 3.1 before 3.1.14, and 3.2 before 3.2.10, HTTP requests for URLs with trailing newlines could bypass upstream access control based on URL paths. This issue has low severity, according to the Django security policy.

GHSA-xgxc-v2qg-chmh:
In Django 2.2 before 2.2.20, 3.0 before 3.0.14, and 3.1 before 3.1.8, MultiPartParser allowed directory traversal via uploaded files with suitably crafted file names. Built-in upload handlers were not affected by this vulnerability.

GHSA-xpfp-f569-q3p2:
Django 3.1.x before 3.1.13 and 3.2.x before 3.2.5 allows QuerySet.order_by SQL injection if order_by is untrusted input from a client of a web application.
```
