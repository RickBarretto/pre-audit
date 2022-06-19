from unittest import mock

import pytest

import responses
import requests

from src.core.fetch_api import OsvApi
from src.core.utils.exceptions import PackageNotFound


class TestApi:
    @responses.activate
    def test_api_ok(self):

        responses.add(
            method="POST",
            url="https://api.osv.dev/v1/query",
            json={
                "vulns": [{"id": "GHSA-xxxx-xxxx-xxxx"}, {"id": "GHSA-yyyy-yyyy-yyyy"}]
            },
            status=200,
        )

        req = requests.post("https://api.osv.dev/v1/query")

        assert req.json() == {
            "vulns": [{"id": "GHSA-xxxx-xxxx-xxxx"}, {"id": "GHSA-yyyy-yyyy-yyyy"}]
        }
        assert req.status_code == 200

    @responses.activate
    def test_requests_with_wrong_package(self):

        responses.add(
            method="POST",
            url="https://api.osv.dev/v1/query",
            json={},
            status=200,
        )

        req = requests.post("https://api.osv.dev/v1/query")
        assert req.json() == {}
        assert req.status_code == 200


class TestExceptions:
    @mock.patch("src.core.fetch_api.requesting.fetch")
    def test_package_not_found(self, mocked_fetch, printer):

        mocked_fetch.return_value = {}

        with pytest.raises(PackageNotFound) as err:
            OsvApi("FakePkg", "3.2").fetch()
        assert True
        printer("Exception tested: {0}".format(err))

    @responses.activate
    def test_http_errors(self, printer):

        error404 = responses.Response(
            method="POST",
            url="https://api.osv.dev/v1/query",
            status=404,
        )

        error512 = responses.Response(
            method="POST",
            url="https://api.osv.dev/v1/query",
            status=512,
        )

        responses.add(error404)
        responses.add(error512)

        with pytest.raises(requests.HTTPError) as err:
            req_4xx = requests.post("https://api.osv.dev/v1/query")
            req_4xx.raise_for_status()
        assert req_4xx.status_code == 404
        printer("Exception tested: {0}".format(err))

        with pytest.raises(requests.HTTPError) as err:
            req_5xx = requests.post("https://api.osv.dev/v1/query")
            req_5xx.raise_for_status()
        assert req_5xx.status_code == 512
        printer("Exception tested: {0}".format(err))
