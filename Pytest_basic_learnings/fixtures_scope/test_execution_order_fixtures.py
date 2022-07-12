import pytest
import logging


@pytest.fixture(scope="session")
def session():
    print("scope session")


@pytest.fixture(scope="package")
def package():
    print("scope package")


@pytest.fixture(scope="module")
def module():
    print("scope module")


@pytest.fixture(scope="class")
def class_():
    print("scope class")


@pytest.fixture(scope="function")
def function():
    print("scope function")


def test_order(module, class_, session, function, package):
    assert True