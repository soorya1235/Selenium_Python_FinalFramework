import pytest

@pytest.fixture(scope='class')
def class_scope_fixture():
    print("class level")

@pytest.fixture(scope='session')
def session_scope_fixture():
    print("session level")

@pytest.fixture(scope='module')
def module_scope_fixture():
    print("module_level")

@pytest.fixture(scope='function')
def function_scope_fixture():
    print("function level")

def test_demo(class_scope_fixture,session_scope_fixture,module_scope_fixture,function_scope_fixture):
    print("hello world")