from sympy.logic.boolalg import And, Or, Not, Nand, Nor
from sympy.logic.boolalg import to_cnf
from sympy import symbols
import sys

class InputMaker:
    def __init__(self):
        self.inputs = {}

    def __getitem__(self, key: int):
        if key in self.inputs:
            return self.inputs[key]
        else:
            self.inputs[key] = symbols(f'x{key}')
            return self.inputs[key]

    def n_inputs(self):
        assert len(self.inputs) == max(self.inputs.keys()) + 1
        return len(self.inputs)

inp = InputMaker()
with open(sys.argv[1]) as f:
    tree = eval(f.read())

print(to_cnf(tree))