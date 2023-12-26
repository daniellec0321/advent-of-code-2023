import sys

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
        rules = dict() # Key: the label. Value: a function that returns where to go
        while (line := stream.readline().strip()):
            label = line.split('{')[0]
            curr_rules = line.split('{')[1][:-1].split(',')
            rules[label] = curr_rules
            
        start_points = [(label, idx, bad_values.copy()) for label, vals in rules.items() for idx, val in enumerate(vals) if val[-1] == 'R']

        while start_points:
            curr_label, curr_idx, curr_bad_values = start_points.pop()
            # Check if the label is "in"



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()