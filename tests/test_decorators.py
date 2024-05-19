import pytest
import os
from src.decorators import log


def test_log_file(): #file_success
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x * y
    result = example_function(5, 100)
    with open(os.path.join(r"mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function ok\n"
    assert result == 500


def test_log_file_raise(): #file_failure
    @log(filename="mylog.txt")
    def example_function(x, y):
        raise TypeError ("Что-то пошло не так")

    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function(5, 100)
    with open(os.path.join(r"mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function error: TypeError. Inputs: (5, 100), {}\n"


def test_log_console(capsys): #console_success
    @log()
    def example_function(x, y):
        return x * y

    result = example_function(5, 100)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok\n"
    assert result == 500


def test_log_console_raise(capsys):  #console_failure
    @log()
    def example_function(x, y):
        raise ValueError("Что-то пошло не так")

    with pytest.raises(ValueError, match="Что-то пошло не так"):
        example_function(5, 100)

    captured = capsys.readouterr()
    assert captured.out == "example_function error: ValueError. Inputs: (5, 100), {}\n"