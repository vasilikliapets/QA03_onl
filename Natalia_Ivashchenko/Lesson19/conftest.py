import pytest
import os
import datetime


@pytest.fixture(scope="session")
def timer():
    start = datetime.datetime.now()
    print('Start time:', start.time())
    yield start
    end = datetime.datetime.now()
    print('End time:', end.time())


@pytest.fixture(scope="module")
def file_name():
    print('File name:', os.path.basename(__file__))


@pytest.fixture
def info_for_test(timer):
    start_test = datetime.datetime.now() - timer
    print('Passed since the session:', start_test)


@pytest.fixture
def fixture_name(request):
    print(request.fixturenames)
