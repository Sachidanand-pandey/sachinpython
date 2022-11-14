import pytest
@pytest.fixture()
def setup():
    print('once before every test method')
def testmethod1(setup):
    print('this is my first method')
def testmethod2(setup):
    print('this is my second method')
def testmethod3(setup):
    print('this is third method')
def testmethod4(setup):
    print('this is fourth test method')
def testmethod5(setup):
    print('this is fifth test method')
def testmethod6(setup):
    print('this is sixth test method')
def testmethod7(setup):
    print('this is seventh test method')
