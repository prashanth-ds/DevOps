import unittest
from Calculator import Calculator


class UnitTesting(unittest.TestCase):

    def setUp(self):
        self.addition = Calculator("10+15")
        self.subtraction = Calculator("10-5")
        self.multiplication = Calculator("11*11")
        self.multiple_operands = Calculator("1+2+3")
        self.multiple_operators = Calculator("2+2*5")
        self.invalid_operator = Calculator("2/2")

    def test_add(self):
        addition = self.addition.evaluate()
        self.assertEqual(addition, 25)

    def test_sub(self):
        subtraction = self.subtraction.evaluate()
        self.assertEqual(subtraction, 5)

    def test_mul(self):
        multiplication = self.multiplication.evaluate()
        self.assertEqual(multiplication, 121)

    # def test_operands(self):
    #     multiple_operands = self.multiple_operands.evaluate()
    #     self.assertEqual(multiple_operands, 6)
    #
    # def test_MultipleOperator(self):
    #     multiple_operators = self.multiple_operators.evaluate()
    #     self.assertEqual(multiple_operators, 12)
    #
    # def test_operator(self):
    #     invalid_operator = self.invalid_operator.evaluate()
    #     self.assertEqual(invalid_operator, 1)


if __name__ == '__main__':
    unittest.main()
