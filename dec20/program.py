import sys
from queue import Queue

class Puzzle1():

    class flipflop():
        def __init__(self):
            self.state = 'off'
            self.outputs = list()
        def rec_pulse(self, pulse: str, inp=None) -> str:
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
        high_pulses = dict()
        low_pulses = dict()
        init_state = list()
        for label, var in vars.items():
            if self.is_conjunction(var):
                for s in var.inputs.values():
                    init_state.append(s)
            elif self.is_flipflop(var):
                init_state.append(var.state)
        states[tuple(init_state)] = 0
        high_pulses[0] = 0
        low_pulses[0] = 0
        start_cycle = 1000

        # Loop through pressing the button 1000 times
        for i in range(1, 1001):
            # Queue will be a list of tuples (module, pulse, source)
            curr_high_pulses = 0
            curr_low_pulses = 1
            q = Queue()
            for op in vars['broadcaster'].outputs:
                q.put((op, 'low', 'broadcaster'))
                curr_low_pulses += 1
            while not q.empty():
                curr_label, curr_pulse, pulse_from = q.get()
                out_pulse = ''
                if curr_label in vars:
                    out_pulse = vars[curr_label].rec_pulse(curr_pulse, pulse_from)
                # Add this stuff to the queue
                if out_pulse:
                    for op in vars[curr_label].outputs:
                        q.put((op, out_pulse, curr_label))
                        if out_pulse == 'low':
                            curr_low_pulses += 1
                        else:
                            curr_high_pulses += 1
                
            # Create state by looping through vars
            curr_state = list()
            for label, var in vars.items():
                if self.is_conjunction(var):
                    for s in var.inputs.values():
                        curr_state.append(s)
                elif self.is_flipflop(var):
                    curr_state.append(var.state)
            # Check if that has been encountered already
            curr_state = tuple(curr_state)
            high_pulses[i] = curr_high_pulses
            low_pulses[i] = curr_low_pulses

            if curr_state in states:
                # add up everything and break
                start_cycle = states[curr_state]
                break
            states[curr_state] = i

        total_high_pulses = 0
        total_low_pulses = 0
        # Calculate middle stuff
        for j in range(start_cycle+1, i+1):
            total_high_pulses += high_pulses[j]
            total_low_pulses += low_pulses[j]
        if i != start_cycle:
            total_high_pulses *= int((1000 - start_cycle) / (i - start_cycle))
            total_low_pulses *= int((1000 - start_cycle) / (i - start_cycle))
        # Calculate beginning leftover
        for j in range(1, start_cycle+1):
            total_high_pulses += high_pulses[j]
            total_low_pulses += low_pulses[j]

        print(f'The answer to puzzle 1 is {total_high_pulses*total_low_pulses}')



class Puzzle2():

    class flipflop():
        def __init__(self):
            self.state = 'off'
            self.outputs = list()
        def rec_pulse(self, pulse: str, inp=None) -> str:
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

        # Loop through pressing the button 1000 times
        # for i in range(1, 1001):
        i = 1
        while True:
            # Queue will be a list of tuples (module, pulse, source)
            if i % 1000 == 0:
                print(f'On cycle {i}')
            low_to_rx = 0
            high_to_rx = 0
            q = Queue()
            for op in vars['broadcaster'].outputs:
                q.put((op, 'low', 'broadcaster'))
                if op == 'rx':
                    low_to_rx += 1
            while not q.empty():
                curr_label, curr_pulse, pulse_from = q.get()
                out_pulse = ''
                if curr_label in vars:
                    out_pulse = vars[curr_label].rec_pulse(curr_pulse, pulse_from)
                # Add this stuff to the queue
                if out_pulse:
                    for op in vars[curr_label].outputs:
                        q.put((op, out_pulse, curr_label))
                        if op == 'rx' and out_pulse == 'high':
                            high_to_rx += 1
                        elif op == 'rx' and out_pulse == 'low':
                            low_to_rx += 1
            if low_to_rx == 1 and high_to_rx == 0:
                break
            i += 1

        # Answer needs to be greater than 1000
        print(f'The answer to puzzle 2 is {i}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()