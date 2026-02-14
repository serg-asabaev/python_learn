import pytest
from typing import Union

from src.decorators import log

@log()
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Функция которая складывает два числа"""
    return a + b

@log()
def subtract(x, y):
    return x - y

@log()
def multiply(x, y):
    return x * y

@log()
def divide(x, y):
    return x / y

@log()
def test_error():
    raise Exception(f"Test excetpion")


@pytest.mark.parametrize('function, func_name, a, b', [
    (add, 'add', 2, 3),
    (subtract, 'subtract', 8, 5),
    (multiply, 'multiply', 7, 2),
])
def test_log_success(capsys, function, func_name, a, b):
    function(a, b)
    captured = capsys.readouterr()

    assert captured.out == 'Начало работы функции '+func_name+'\n'+func_name+' ok\nКонец работы функции '+func_name+'\n'


@pytest.mark.parametrize('function, func_name, err_type, a, b', [
    (divide, 'divide', 'ZeroDivisionError', 5, 0),

])
def test_log_error(capsys, function, func_name, err_type, a, b):
    function(a, b)
    captured = capsys.readouterr()

    assert captured.out == f'Начало работы функции {func_name}\n'\
                            f'{func_name} error: {err_type}. Inputs: ({a}, {b}), ' + '{}\n'\
                            f'Конец работы функции {func_name}\n'


@pytest.mark.parametrize(
    'function, func_name, err_type',
    [
        (test_error, 'test_error', 'Exception'),
    ]
)
def test_log_error_manual(capsys, function, func_name, err_type):
    function()
    captured = capsys.readouterr()

    assert captured.out == f'Начало работы функции {func_name}\n'\
                            f'{func_name} error: {err_type}. Inputs: (), ' + '{}\n'\
                            f'Конец работы функции {func_name}\n'