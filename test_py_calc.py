import py_calc

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
