import py_calc
import pytest

def test_float_default(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', '4/3'])
    result = py_calc.get_args(monkeypatch)
    assert result == '1.33'

def test_float_default_verbose(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', '-v', '4/3'])
    result = py_calc.get_args(monkeypatch)
    assert result == '4/3 = 1.33'

def test_float_with_precision_defined(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', '-f3', '22/7'])
    result = py_calc.get_args(monkeypatch)
    assert result == '3.143'

def test_float_turn_off_precission(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', '-F', '22/7'])
    result = py_calc.get_args(monkeypatch)
    assert result == '3.142857142857143'

def test_int_output(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', '-F', '12 ** 12'])
    result = py_calc.get_args(monkeypatch)
    assert result == '8916100448256'

def test_with_matematical_expressions(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', 'sin(radians(90))'])
    result = py_calc.get_args(monkeypatch)
    assert result == '1.00'

def test_with_factorial_sign(monkeypatch):
    monkeypatch.setattr("sys.argv", ['', '2 + 5!'])
    result = py_calc.get_args(monkeypatch)
    assert result == '122'

"""
We leave the exception tests for anothe time.

def test_no_valid_expression_fail(monkeypatch):
    with pytest.raises(NameError):
        monkeypatch.setattr("sys.argv", ['', 'command_no_valid'])
        result = py_calc.get_args(monkeypatch)

def test_raises_with_info(monkeypatch):
    with pytest.raises(NameError) as exc_info:
        monkeypatch.setattr("sys.argv", ['', 'command_no_valid'])
        py_calc.get_args(monkeypatch)
    expected = "NameError: name 'comando_no_valid' is not define"
    assert expected in str(exc_info.value)
"""
