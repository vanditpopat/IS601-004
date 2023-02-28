import pytest
from MyCalc import MyCalc

class TestMyCalc:
    # vp645 and 02/27/2023 initializing instance of MyCalc class
    def setup_class(self):
        self.calc = MyCalc()
    
    # vp645 02/27/2023 asserting to check if the add method actually adds values properly
    def test_addition(self):
        assert self.calc.add(3,6) == 9
        assert self.calc.add(2, 10) == 12
        assert self.calc.add(-8, 2) == -6
        assert self.calc.add(-2, -2) == -4
    
    # vp645 02/27/2023 asserting to check if what answer we get is stored and then when added again does it work properly
    def test_addition_with_ans(self):
        ans  = self.calc.add(3, 3)
        assert self.calc.add(ans, 4) == 10

        ans  = self.calc.add(10, 15)
        assert self.calc.add(ans, -18) == 7

        ans  = self.calc.add(-2, 6)
        assert self.calc.add(ans, 120) == 124

        ans  = self.calc.add(2, 2)
        assert self.calc.add(ans, -27) == -23

    # vp645 02/27/2023 asserting to check if the substract method actually subtracts values properly    
    def test_subtraction(self):
        assert self.calc.subtract(5, 2) == 3
        assert self.calc.subtract(-23, 10) == -33
        assert self.calc.subtract(-11, -21) == 10
        assert self.calc.subtract(10, -20) == 30
    
    # vp645 02/27/2023 asserting to check if what answer we get is stored and then when subtracted again does it work properly
    def test_subtraction_with_ans(self):
        ans = self.calc.subtract(5, 2)
        assert self.calc.subtract(ans, 2) == 1

        ans = self.calc.subtract(-23, 10)
        assert self.calc.subtract(ans, 15) == -48

        ans = self.calc.subtract(-11, -21)
        assert self.calc.subtract(ans, -20) == 30

        ans = self.calc.subtract(10, -20)
        assert self.calc.subtract(ans, -22) == 52
    
    # vp645 02/27/2023 asserting to check if the multiply method actually multiplies values properly
    def test_multiplication(self):
        assert self.calc.multiply(2, 2) == 4
        assert self.calc.multiply(3.5, 4) == 14
        assert self.calc.multiply(8.02, 2) == 16.04
        assert self.calc.multiply(-12, 2) == -24
    
    # vp645 02/27/2023 asserting to check if what answer we get is stored and then when multiplied again does it work properly
    def test_multiplication_with_ans(self):
        ans = self.calc.multiply(2, 2)
        assert self.calc.multiply(ans, 2) == 8

        ans = self.calc.multiply(3.5, 4)
        assert self.calc.multiply(ans, 2) == 28

        ans = self.calc.multiply(8.02, 2)
        assert self.calc.multiply(ans, 2.1) == 33.684

        ans = self.calc.multiply(0.2, -0.3)
        assert self.calc.multiply(ans, 3) == -0.18
    
    # vp645 02/27/2023 asserting to check if the divide method actually divides values properly
    def test_division(self):
        assert self.calc.divide(8, 2) == 4
        assert self.calc.divide(6.6, 3.2) == 2.0624999999999996
        assert self.calc.divide(5.5, -2) == -2.75
        assert self.calc.divide(0.6, 2) == 0.3 
    

    # vp645 02/27/2023 asserting to check if what answer we get is stored and then when divided again does it work properly
    def test_division_with_ans(self):
        ans = self.calc.divide(8, 2)
        assert self.calc.divide(ans, 2) == 2

        ans = self.calc.divide(6.6, 3.2)
        assert self.calc.divide(ans, 1.1) == 1.8749999999999996

        ans = self.calc.divide(5.5, -2)
        assert self.calc.divide(ans, 2) == -1.375

        ans = self.calc.divide(0.6, 2)
        assert self.calc.divide(ans, 0.01) == 30.0
    