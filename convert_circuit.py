import sys
from dataclasses import dataclass

# classes for eval/parsing
@dataclass
class Gate:
    pass

@dataclass
class And(Gate):
    l: Gate
    r: Gate
    t = 'and'

@dataclass
class Or(Gate):
    l: Gate
    r: Gate
    t = 'or'

@dataclass
class Nand(Gate):
    l: Gate
    r: Gate
    t = 'nand'

@dataclass
class Nor(Gate):
    l: Gate
    r: Gate
    t = 'nor'

@dataclass
class Not(Gate):
    c: Gate
    t = 'not'

@dataclass
class Input(Gate):
    g_id: int
    t = 'inp'

class InputMaker:
    def __init__(self):
        self.inputs = {}

    def __getitem__(self, key: int):
        if key in self.inputs:
            return self.inputs[key]
        else:
            self.inputs[key] = Input(key)
            return self.inputs[key]

    def n_inputs(self):
        assert len(self.inputs) == max(self.inputs.keys()) + 1
        return len(self.inputs)

def main():
    inp = InputMaker()
    with open(sys.argv[1]) as f:
        tree = eval(f.read())

    # printing
    cur_g_id = inp.n_inputs()
    lines = []

    def process_circuit(g: Gate) -> int:
        nonlocal cur_g_id, lines

        if isinstance(g, Input):
            lines.append(f'{g.t} {g.g_id}')
            return g.g_id
        elif isinstance(g, And) or isinstance(g, Or) or isinstance(g, Nand) or isinstance(g, Nor):
            l_id = process_circuit(g.l)
            r_id = process_circuit(g.r)
            lines.append(f'{g.t} {cur_g_id} {l_id} {r_id}')
            ret = cur_g_id
            cur_g_id += 1
            return ret
        elif isinstance(g, Not):
            c_id = process_circuit(g.c)
            lines.append(f'{g.t} {cur_g_id} {c_id}')
            ret = cur_g_id
            cur_g_id += 1
            return ret
        else: assert 0, "Invalid gate type"

    # print
    lines.append(str(inp.n_inputs()))
    process_circuit(tree)
    lines.insert(1, str(cur_g_id))
    with open(sys.argv[2], 'w') as f:
        for line in lines:
            # print(line)
            f.write(line + '\n')
    
    print(f'Wrote {len(lines)} gates with {inp.n_inputs()} inputs')

if __name__ == '__main__':
    main()