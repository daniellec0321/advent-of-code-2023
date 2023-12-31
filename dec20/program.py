import sys
from queue import Queue

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
        
    class broadcaster():
        def __init__(self):
            self.outputs = list()
        
    def is_flipflop(self, obj):
        return isinstance(obj, Puzzle1.flipflop)
    
    def is_conjunction(self, obj):
        return isinstance(obj, Puzzle1.conjunction)
    
    def is_broadcaster(self, obj):
        return isinstance(obj, Puzzle1.broadcaster)

    def solve_puzzle(self, stream=sys.stdin):
        
        # Read in input
        vars = dict() # Key: string of the label. Value: the object
        for line in stream.readlines():
            source = line.split(' -> ')[0]
            outputs = [x.strip() for x in line.split(' -> ')[1].split(', ')]
            if source[0] == '%':
                new_obj = self.flipflop()
                new_obj.outputs = outputs
                vars[source[1:]] = new_obj
            elif source[0] == '&':
                new_obj = self.conjunction()
                new_obj.outputs = outputs
                vars[source[1:]] = new_obj
            else:
                new_obj = self.broadcaster()
                new_obj.outputs = outputs
                vars[source] = new_obj

        # Set up the inputs of all of the conjunctions
        for label, var in vars.items():
            for op in var.outputs:
                if op in vars and self.is_conjunction(vars[op]):
                    vars[op].inputs[label] = 'low'

        # Set up states
        states = dict() # Key: tuple, value: cycle num
        init_state = list()
        for label, var in vars.items():
            if self.is_conjunction(var):
                for s in var.inputs.values():
                    init_state.append(s)
            elif self.is_flipflop(var):
                init_state.append(var.state)
        states[tuple(init_state)] = 0

        # Loop through pressing the button 1000 times
        for i in range(1000):
            # Update states
            # Queue will be a list of tuples (module, pulse)
            q = Queue()
            for op in vars['broadcaster'].outputs:
                q.put((op, 'low'))
            while not q.empty():
                curr_label, curr_pulse = q.get()
                
            # Check if that has been encountered already


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