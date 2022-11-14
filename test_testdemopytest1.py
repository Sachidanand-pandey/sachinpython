import pytest
@pytest.fixture()
def setup():
    print('once before every test method')
    yield
    print('once after every method')
def testmethod1(setup):
    print('this is my first method')
def testmethod2(setup):
    print('this is my second method')
def testmethod3(setup):
    print('this is third method')

