import pytest
from calculator import BasicCalculator, AccurateCalculator

@pytest.fixture
def basic_calculator():
    return BasicCalculator()

@pytest.fixture
def accurate_calculator():
    return AccurateCalculator(digits=2)
