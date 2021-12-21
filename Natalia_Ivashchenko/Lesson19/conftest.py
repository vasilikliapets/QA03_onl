import pytest
import os
import datetime


@pytest.fixture(scope="module", autouse=True)
def timer():
    start = datetime.datetime.now()
    print('Start time:', start.time())
    yield start
    end = datetime.datetime.now()
    print('End time:', end.time())


@pytest.fixture(scope="module", autouse=True)
def file_name():
    print('File name:', os.path.basename(__file__))


@pytest.fixture(autouse=True)
def info_for_test(timer):
    start_test = datetime.datetime.now() - timer
    print('Passed since the session:', start_test)


@pytest.fixture(autouse=True)
def fixture_name(request):
    print(request.fixturenames)
