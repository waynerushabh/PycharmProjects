# import pytest
# import my_functions_file
import pytest

import my_functions_file


def test_add():
    result = my_functions_file.add(1, 4)
    assert result == 5


def test_divide():
    result = my_functions_file.divide(10, 5)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises((ZeroDivisionError)):
        my_functions_file.divide(10, 0)
