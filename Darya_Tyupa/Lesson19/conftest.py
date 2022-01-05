import pytest
from datetime import datetime


@pytest.fixture(scope='session')  # выводим в начале и в конце сессии время
def time_of_execution():
    """This fixture shows start time and end time of session"""
    start_time = datetime.now()
    print(f'Start time is {start_time}')
    yield start_time
    print('End time is', datetime.now())


@pytest.fixture(scope='module')
def scope_name(request):
    """This fixture prints name of module"""
    print(f'Module name is {request.node.name}')  # этот метод выводит имя скоупа


@pytest.fixture  # здесь можно было использовать (autouse=True), но вы сказали лучше так не делать
def time_between_executions(time_of_execution):
    """This fixture counts and prints time between start time of session and start time of each test"""
    print('Time =', (datetime.now() - time_of_execution).total_seconds())
