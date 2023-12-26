import sys
from queue import Queue

class Puzzle1():

    def create_function(self, rules: list[str]):
        def func(vars: dict) -> str:
            for rule in rules[:-1]:
                r, curr_dest = rule.split(':')
                label = r[0]
                comp = r[1]
                num = int(r[2:])
                if comp == '<' and vars[label] < num:
                    return curr_dest
                elif comp == '>' and vars[label] > num:
                    return curr_dest
            return rules[-1]
        return func

    def solve_puzzle(self, stream=sys.stdin):

        # Read in rules
        rules = dict() # Key: the label. Value: a function that returns where to go
        while (line := stream.readline().strip()):
            label = line.split('{')[0]
            curr_rules = line.split('{')[1][:-1].split(',')
            rules[label] = self.create_function(curr_rules)
            
        # Read in all the vars
        total = 0
        while (line := stream.readline().strip()):
            vars = dict()
            for p in line[1:-1].split(','):
                var, num = p.split('=')
                vars[var] = int(num)
            label = 'in'
            while label != 'A' and label != 'R':
                label = rules[label](vars)
            if label == 'A':
                total += sum(vars.values())
        
        print(f'The answer to puzzle 1 is {total}')



class Puzzle2():

    def solve_puzzle(self, stream=sys.stdin):
        bad_values = {'x': set(), 'm': set(), 'a': set(), 's': set()}

        # Find all the rules that end in rejection
        # Find path by going from R -> in
        rules = dict() # Key: the label. Value: the list of rules
        presence = dict() # Key: the label. Value: the set of tuples of (label, idx) where this label is present
        while (line := stream.readline().strip()):
            label = line.split('{')[0]
            curr_rules = line.split('{')[1][:-1].split(',')
            rules[label] = curr_rules
            for idx, rule in enumerate(curr_rules):
                dest = rule.split(':')[1] if ':' in rule else rule
                if dest not in presence:
                    presence[dest] = set()
                presence[dest].add((label, idx))

        # start_points = [(label, idx, bad_values.copy()) for label, vals in rules.items() for idx, val in enumerate(vals) if val[-1] == 'R']
        # start_points = [(label, bad_values.copy()) for label in presence['R']]
        start_points = Queue()
        for label, idx in presence['R']:
            start_points.put((label, 'R', idx, bad_values.copy()))

        total_bad = 0
        while not start_points.empty():
            # curr_label, curr_idx, curr_bad_values = start_points.pop()
            # Check if the label is "in"
            label, dest, idx, curr_bad_values = start_points.get()
            print(f'looking at label {label} with dest {dest}, idx {idx}')
            # Look through the label and find the conditions that get to the dest
        #     perform_nots = True if rules[label][-1] == dest else False
        #     print('The rules are:')
        #     for rule in rules[label]:
        #         print(rule)
        #     for rule in rules[label][:-1]:
        #         condition, res = rule.split(':')
        #         if perform_nots and res != dest:
        #             if '<' in condition:
        #                 var, num = condition.split('<')
        #                 num = int(num)
        #                 print(f'For rule {rule}, adding values to var {var} from {num} to {4000}')
        #                 for i in range(num, 4001):
        #                     curr_bad_values[var].add(i)
        #             else:
        #                 var, num = condition.split('>')
        #                 num = int(num)
        #                 print(f'For rule {rule}, adding values to var {var} from {0} to {num}')
        #                 for i in range(0, num+1):
        #                     curr_bad_values[var].add(i)
        #         elif res == dest:
        #             if '<' in condition:
        #                 var, num = condition.split('<')
        #                 num = int(num)
        #                 print(f'For rule {rule}, adding values to var {var} from {0} to {num-1}')
        #                 for i in range(0, num):
        #                     curr_bad_values[var].add(i)
        #             else:
        #                 var, num = condition.split('>')
        #                 num = int(num)
        #                 print(f'For rule {rule}, adding values to var {var} from {num+1} to {4000}')
        #                 for i in range(num+1, 4001):
        #                     curr_bad_values[var].add(i)
        #     # If label is 'in', add to the global thing and stop
        #     if label == 'in':
        #         total = 1
        #         for var in curr_bad_values:
        #             total *= len(curr_bad_values[var])
        #         total_bad += total
        #         continue
        #     # Add the labels and bad values to the queue
        #     for l in presence[label]:
        #         start_points.put((l, label, curr_bad_values.copy()))
        #     print('--------------------')
        
        # # Find the number of good values
        # good_values = pow(4000, 4) - total_bad
        # print(f'The answer to puzzle 2 is {good_values}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()