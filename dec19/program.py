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
        good_values = {'x': set(), 'm': set(), 'a': set(), 's': set()}

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

        start_points = Queue()
        for label, idx in presence['A']:
            start_points.put((label, 'A', idx, good_values.copy()))

        total_good = 0
        while not start_points.empty():
            # Check if the label is "in"
            label, dest, idx, curr_good_values = start_points.get()

            for rule in rules[label][:idx]:
                condition, res = rule.split(':')
                if '<' in condition:
                    var, num = condition.split('<')
                    num = int(num)
                    for i in range(num, 4001):
                        curr_good_values[var].add(i)
                else:
                    var, num = condition.split('>')
                    num = int(num)
                    for i in range(0, num+1):
                        curr_good_values[var].add(i)

            # Check last value
            if idx != len(rules[label])-1:
                condition = rules[label][idx].split(':')[0]
                if '<' in condition:
                    var, num = condition.split('<')
                    num = int(num)
                    for i in range(0, num):
                        curr_good_values[var].add(i)
                else:
                    var, num = condition.split('>')
                    num = int(num)
                    for i in range(num+1, 4001):
                        curr_good_values[var].add(i)

            # Check if the label is 'in', which means we're at the end
            if label == 'in':
                total = 1
                to_add = dict()
                for var in curr_good_values:
                    to_add[var] = curr_good_values[var] - good_values[var]
                    print(f'len of total is {len(good_values[var])}, len of curr is {len(curr_good_values[var])}, len of to add is {len(to_add[var])}')
                    total *= len(to_add[var])
                    good_values[var] = good_values[var] | curr_good_values[var]
                total_good += total
                continue # tally up stuff and add to total good

            # Add to the queue
            for l, idx in presence[label]:
                start_points.put((l, label, idx, curr_good_values.copy()))

        print(f'The answer to puzzle 2 is {total_good}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()