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
        print("This is Evaluation on 30th august")

    def test_add(self):
        addition = self.addition.evaluate()
        self.assertEqual(addition, 25, f"Addition is {addition}")

    def test_sub(self):
        subtraction = self.subtraction.evaluate()
        self.assertEqual(subtraction, 5, f"Subtraction is {subtraction}")

    def test_mul(self):
        multiplication = self.multiplication.evaluate()
        self.assertEqual(multiplication, 121, f"Multiplication is {multiplication}")

    def test_operands(self):
        multiple_operands = self.multiple_operands.evaluate()
        self.assertEqual(multiple_operands, 'Same Operator Used More than once', 'Same Operator Used More than once')

#     def test_MultipleOperator(self):
#         multiple_operators = self.multiple_operators.evaluate()
#         self.assertEqual(multiple_operators, 'Operators Used Multiple times', 'Operators Used Multiple times')

#     def test_operator(self):
#         invalid_operator = self.invalid_operator.evaluate()
#         self.assertEqual(invalid_operator, 'Operator Invalid', 'Operator Invalid')


if __name__ == '__main__':
    unittest.main()
