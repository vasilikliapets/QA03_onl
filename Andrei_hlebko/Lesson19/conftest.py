import os
import sys
import time
from datetime import datetime

import pytest


@pytest.fixture(scope="module")
def check_time():
    """
    The fixture print Begin test and Finish test
    """
    start_time = time.time()
    print('\n Начало теста:', datetime.now())
    yield start_time
    print('\n' "Конец теста:", datetime.now())


@pytest.fixture(scope="module")
def name_file():
    """
    This fixture print name started test
    """
    print("Имя файла из которого запущен тест:", os.path.basename(sys.argv[-1]))


@pytest.fixture()  # по умолчанию scope="function"
def time_session_test(check_time):
    """
    The fixture show time interval - Begin session and begin the test
    """
    print("\n""Время с момента запуска сессии:", abs(check_time - time.time()))
