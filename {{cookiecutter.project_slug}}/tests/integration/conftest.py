"""
pytest fixtures for {{ cookiecutter.project_name }} integration tests
"""
import pytest


@pytest.fixture(scope='session')
def domain():
    """
    :return: Domain of the running service.
    """
    return 'http://0.0.0.0:5000'
