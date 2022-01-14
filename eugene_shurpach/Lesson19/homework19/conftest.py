import time
import pytest

@pytest.fixture(scope='session')
def get_time():
    start = time.perf_counter()
    print(f"\nВремя старта: {start}")
    yield start
    print(f"\nВремя завершения: {time.perf_counter()}")


@pytest.fixture(scope='module')
def get_name(request):  # фикстура вывода имени модуля
    print(f'Тесты из файла: {request.node.name}')

@pytest.fixture
def count_time(get_time):
    end = time.perf_counter()
    print(f"\nВремя выполения от начала: {end - get_time}")
