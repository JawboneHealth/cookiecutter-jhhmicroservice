"""
Minimal integration test to verify the healthcheck endpoint.
"""
import httplib
import requests


def test_healthz(domain):
    """
    Verify the healthcheck responds

    :param domain: domain of the running service
    """
    resp = requests.get('{}/healthz'.format(domain))
    assert resp.status_code == httplib.OK
