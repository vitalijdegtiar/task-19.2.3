import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multyply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multyply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 2) == 6

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 8, 2) == 10

