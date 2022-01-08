import time
import pytest

start = time.perf_counter()


@pytest.fixture(scope='module')
def get_time():
    print(f"\nВремя старта: {start}")
    yield
    print(f"\nВремя завершения: {time.perf_counter()}")


@pytest.fixture(scope='module')
def get_name(request):  # фикстура вывода имени модуля
    print(f'Тесты из файла: {request.node.name}')

@pytest.fixture
def count_time():
    end = time.perf_counter()
    print(f"\nВремя выполения от начала: {end - start}")
