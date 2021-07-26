import operator


class Calculator:

    def __init__(self, expression):
        self.exp = expression
        self.operators = ['+', '-', '*']
        self.operation = ''
        self.integers = []
        self.eval = {'+': operator.add, '-': operator.sub, '*': operator.mul}

    def __str__(self):
        # return f"Entered expression: {self.exp}"
        return f"{self.integers}"

    def __validate(self):
        """
        Here we validate the expression, where two positive integers and operators (+,-,*) are valid.
        :return: Boolean : True for valid expression, and vice versa.
        """

        for op in self.operators:
            if op in self.exp:
                self.operation = op
                try:
                    self.integers = list(map(int, self.exp.split(self.operation)))
                    if len(self.integers) == 2:
                        return "Correct"
                    elif len(self.integers) < 2:
                        return "No Valid Expression"
                    else:
                        # control comes here if operator is same, as the split func will split according to initially
                        # found operator and if length of self.integers is more than 2 ofcourse there are more than
                        # two operands with same operator
                        return "Same Operator Used More than once"
                except ValueError:
                    # control comes here when different operators are used, ofcourse more than 2 operands
                    return "Operators Used Multiple times"

    def evaluate(self):
        """
        This method will evaluate the validated expression
        :return: The Evaluated Output.
        """

        condition = self.__validate()

        if condition == "Correct":
            return self.eval[self.operation](*self.integers)
        else:
            if condition is None:
                return "Operator Invalid"
            return condition


obj = Calculator("2/4")
print(obj.evaluate())
