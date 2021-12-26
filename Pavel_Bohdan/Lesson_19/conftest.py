import lower_case, type_float, simbol
from datetime import datetime
import pytest
import time
import os
import sys


start_tests = time.time()

@pytest.fixture(scope='session')
def file_name():
    print('Тест', os.path.basename(sys.argv[3]))

@pytest.fixture(scope='session')
def start_time():
    print(' Начало теста', datetime.now())
    yield start_time
    print('Конец теста', datetime.now())

@pytest.fixture(scope='function')
def run_time():
    yield run_time
    print(' Время выполнения теста с начала сессии: ', round((time.time() - start_tests), 3), 'sec')

