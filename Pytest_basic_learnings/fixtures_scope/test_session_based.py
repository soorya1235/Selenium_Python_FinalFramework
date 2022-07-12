import json
import logging

import pytest

"""
Session is consider for the execution of 1 test of all the test methods.
"""

@pytest.fixture(scope="session")
def read_config():
    with open("app.json") as f:
        config = json.load(f)
        logging.info("Read config")
    return config

@pytest.fixture(scope="session")
def scope_session():
    print("called frist")
    yield
    print("Called end of sesion")

def test1(read_config,scope_session):
    logging.info("Test function 1")
    #assert read_config == {}c
    #assert read_config ==  {'a': 1, 'b': 2}

def test2(read_config,scope_session):
    logging.info("Test function 2")
    assert read_config ==  {'a': 1, 'b': 2}
