import pytest

@pytest.fixture()
def setup():
    print('before all the method')
    yield
    print('after all the method') 
def testmethod1(setup):
    print('this is my first method')
def testmethod2(setup):
    print('this is my second method')
def testmethod3(setup):
    print('this is my third method')

