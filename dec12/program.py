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

    def helper(self, groups: list[str], contigs: list[int]) -> int:
        if not (groups and contigs):
            return 0
        
        # Base case: one contig left
        if len(contigs) == 1:
            line = '#' * contigs[0]
            for group in groups:
                pass

        
        counts = 0
        # Loop through each possible starting position
        for start_pos in range(0, len(groups[0])-contigs[0]):
            end_pos = start_pos + contigs[0]
            print(f'Contig is {contigs[0]}, line is {groups[0]}')
            print(f'Start pos is {start_pos}, end pos is {end_pos}')
            # Check that beginning and end are ? not #
            if len(groups[0]) > 1:
                if start_pos > 0 and groups[0][start_pos-1] == '#':
                    continue
                if end_pos < len(groups[0]) and groups[0][end_pos] == '#':
                    continue
            # If valid, then recurse
            # check if we can break up the line
            new_groups = groups.copy()[1:]
            if end_pos < len(groups[0]) - 1:
                print('hiiiiiiiii')
                add_this = groups[0][end_pos:]
                new_groups.insert(0, add_this)
            counts += self.helper(new_groups, contigs[1:])
        
        return counts



    def solve_puzzle(self):
        counts = 0
        for l, c in [(x.strip().split(' ')[0], \
         list(map(int, x.strip().split(' ')[1].split(',')))) \
         for x in sys.stdin.readlines()]:
            line = ''
            contigs = list()
            for _ in range(4):
                line += (l + '?')
                contigs += c
            contigs += c
            line += l
            # Split line by periods
            groups = list(filter(lambda l: l != '', line.split('.')))
            groups = ['#??#', '###']
            contigs = [2, 1, 3]
            counts += self.helper(groups, contigs)
            # print(line)
            # print(groups)
            # print(contigs)

            break

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