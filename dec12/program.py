import sys
from itertools import combinations

def puzzle1():

    counts = 0
    for line, contig in [(x.strip().split(' ')[0], \
     list(map(int, x.strip().split(' ')[1].split(',')))) \
     for x in sys.stdin.readlines()]:
        
        unknowns = [i for i, ch in enumerate(line) if ch == '?']
        to_find = sum(contig) - len([i for i, ch in enumerate(line) if ch == '#'])
        for combo in combinations(unknowns, to_find):
            test = list(line)
            for idx in combo:
                test[idx] = '#'
            test = (''.join(test)).replace('?', '.')
            # Verify test
            groups = list(filter(lambda l: (l != '') and (l != '.'), test.split('.')))
            if len(groups) != len(contig):
                continue
            valid = True
            for idx, g in enumerate(groups):
                if len(g) != contig[idx]:
                    valid = False
                    break
            if valid:
                counts += 1

    print(f'The answer to puzzle 1 is {counts}')



class Puzzle2():

    def helper(self, groups: list[str], contigs: list[int]):

        # Base case: no groups left but there are contigs left
        if (not groups) and contigs:
            return 0

        # Base case: empty contings and no # left in groups
        if not contigs:
            for group in groups:
                if '#' in group:
                    return 0
            return 1

        # See how many contigs can fit in the group
        group = groups[0]
        for idx in range(0, len(contigs)):
            '''
            Example: group is ?#??
            contig is 1
            '''

            # Find farthest point
            first_pound = group.find('#')

            contigs_to_fit = contigs[0:idx+1]
            space_needed = sum(contigs_to_fit) + (len(contigs_to_fit)-1)
            # Number of recursions will be the amount of space left in the group
            num_recursions = len(group) - space_needed + 1

    def solve_puzzle(self):

        counts = 0
        for line, contig in [(x.strip().split(' ')[0], \
         list(map(int, x.strip().split(' ')[1].split(',')))) \
         for x in sys.stdin.readlines()]:

            pass
        

        print(f'The answer to puzzle 2 is {counts}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()
        SOL.solve_puzzle()