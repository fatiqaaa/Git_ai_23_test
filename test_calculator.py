import pytest
from calculator import Calculator, PreciseCalculator

@pytest.fixture
def basic_calc():
    return Calculator()

@pytest.fixture
def custom_precise_calc():
    return PreciseCalculator(precision=2)

@pytest.mark.parametrize("num1, num2, rounding, output", [
    (3.14159, 2, 2, 5.14),
    (2.71828, 3, 3, 5.718),
    (1.23456, 7, 1, 8.2),
    (4.6789, 5, 3, 9.679)
])
def test_add_precision(custom_precise_calc, num1, num2, rounding, output):
    custom_precise_calc.precision = rounding
    assert custom_precise_calc.add(num1, num2) == output

@pytest.mark.parametrize("num1, num2, rounding, output", [
    (3.14159, 1, 2, 2.14),
    (10.56789, 5, 3, 5.568),
    (6.9823, 2, 1, 5.0)
])
def test_subtract_precision(custom_precise_calc, num1, num2, rounding, output):
    custom_precise_calc.precision = rounding
    assert custom_precise_calc.subtract(num1, num2) == output

@pytest.mark.parametrize("num1, num2, output", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_basic(basic_calc, num1, num2, output):
    assert basic_calc.add(num1, num2) == output

@pytest.mark.parametrize("num1, num2, output", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2)
])
def test_subtract_basic(basic_calc, num1, num2, output):
    assert basic_calc.subtract(num1, num2) == output

@pytest.mark.parametrize("base, exp, result", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),
    (10, -1, 0.1)
])
def test_power_function(basic_calc, base, exp, result):
    assert basic_calc.power(base, exp) == pytest.approx(result)

@pytest.mark.parametrize("num1, num2, product", [
    (3, 5, 15),
    (-1, 5, -5),
    (-2, -3, 6),
    (2.5, 4, 10.0),
    (0.1, 0.2, 0.02)
])
def test_multiplication(basic_calc, num1, num2, product):
    assert basic_calc.multiply(num1, num2) == pytest.approx(product, rel=1e-9)

@pytest.mark.parametrize("dividend, divisor, quotient", [
    (10, 2, 5),
    (5, 2, 2.5)
])
def test_division(basic_calc, dividend, divisor, quotient):
    assert basic_calc.divide(dividend, divisor) == quotient

def test_division_by_zero(basic_calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        basic_calc.divide(5, 0)

@pytest.mark.parametrize("num, fact", [
    (0, 1),
    (1, 1),
    (5, 120),
    (3, 6),
    (7, 5040)
])
def test_factorial(basic_calc, num, fact):
    assert basic_calc.factorial(num) == fact

def test_factorial_invalid(basic_calc):
    with pytest.raises(ValueError):
        basic_calc.factorial(-5)

@pytest.mark.parametrize("index, fib", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (7, 13)
])
def test_fibonacci_series(basic_calc, index, fib):
    assert basic_calc.fibonacci(index) == fib

def test_fibonacci_negative(basic_calc):
    with pytest.raises(ValueError):
        basic_calc.fibonacci(-2)
