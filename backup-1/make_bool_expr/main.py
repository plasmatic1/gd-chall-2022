import random
import numpy as np
from pysat.solvers import Solver

SEED = 10203040

N = 5
M = 1000
P = 0.05 # value of P for geometric distro for generating expression

# expr gen class
class ExpressionGenerator:
    block_size = 10000

    def __init__(self, n, p, solution):
        self.n = n
        self.p = p
        self.solution = solution
        self.all_vars = list(range(1, n+1))
        self.buffer = []
    
    def gen_size(self):
        if not self.buffer:
            self.buffer = list(np.random.geometric(self.p, ExpressionGenerator.block_size))
        
        return max(2, min(self.n, self.buffer.pop()))
    
    def gen_expression(self):
        size = self.gen_size()
        return [x if self.solution[x-1] else -x for x in random.sample(self.all_vars, k=size)]


# init rng
np.random.seed(SEED)
random.seed(SEED)

# init pysat
# pysat.params['data_dirs'] = 'make_bool_expr'

# build expr
state = [random.randint(0, 1) for _ in range(N)]
exprs = []
expr_gen = ExpressionGenerator(N, P, state)

tot_terms = 0
for _ in range(M):
    expr = expr_gen.gen_expression()
    tot_terms += len(expr)
    exprs.append(expr)

print(f'Created initial network, total {M} expressions, {tot_terms} terms')

# solve and extend
s = Solver(name='g4')
for expr in exprs:
    s.add_clause(expr)
assert s.solve()

def has_one(): # checks if soln is unique.  Assumes at least one exists
    found = False

    for _ in s.enum_models():
        if not found:
            found = True
        elif found:
            return False
    
    return True

while not has_one():
    expr = expr_gen.gen_expression()
    tot_terms += len(expr)
    exprs.append(expr)
    print(expr)
    s.add_clause(expr)
    assert s.solve()

    print(f'Solution not unique, added expression with {len(expr)} terms.  Total {len(exprs)} expressions, {tot_terms} terms')

# sanity check soln
for x in s.get_model():
    if x > 0:
        assert state[x-1], f'Got {x} in pysat solution, expected true'
    elif x < 0:
        assert not state[abs(x)-1], f'Got {x} in pysat solution, expected false'

# write to file
with open('expr.txt') as f:
    f.write(f'{N}\n')
    for expr in exprs:
        f.write(f'{",".join(map(str, expr))}\n')