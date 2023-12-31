import sys

class Puzzle1():

    class flipflop():
        def __init__(self):
            self.state = 'off'
            self.outputs = list()
        def rec_pulse(self, pulse: str) -> str:
            if pulse == 'low' and self.state == 'off':
                self.state = 'on'
                return 'high'
            if pulse == 'low' and self.state == 'on':
                self.state = 'off'
                return 'low'
            return ''

    class conjunction():
        def __init__(self):
            self.inputs = dict() # Key: string of input, Value: string of high or low
            self.outputs = list()
        def rec_pulse(self, pulse: str, inp: str) -> str:
            self.inputs[inp] = pulse
            if all([x == 'high' for x in self.inputs.values()]):
                return 'low'
            return 'high'
        
    def is_flipflop(self, obj):
        return isinstance(obj, Puzzle1.flipflop)
    
    def is_conjunction(self, obj):
        return isinstance(obj, Puzzle1.conjunction)

    def solve_puzzle(self, stream=sys.stdin):
        
        # Read in input
        vars = dict() # Key: string of the label. Value: the object
        for line in stream.readlines():
            source = line.split(' -> ')[0]
            outputs = [x.strip() for x in line.split(' -> ')[1].split(', ')]
            print(f'source: {source}, outputs: {outputs}')
            if source[0] == '%':
                new_obj = self.flipflop()
                new_obj.outputs = outputs
                vars[source[1:]] = new_obj
            elif source[0] == '&':
                new_obj = self.conjunction()
                new_obj.outputs = outputs
                vars[source[1:]] = new_obj
            else:
                new_obj = 'broadcaster'
                vars[source] = new_obj


class Puzzle2():
    def solve_puzzle(self, stream=sys.stdin):
        pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()