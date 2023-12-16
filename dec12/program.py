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
        # print(f'Recursing on groups: {groups}, contigs: {contigs}')
        if not (groups and contigs):
            return 0

        # Base case: one contig left
        if len(contigs) == 1:
            found = False
            for group in groups:
                if '#' in group and not found:
                    found = True
                elif '#' in group and found:
                    # print(f'group: {group}, contig: {contigs[0]} - invalid')
                    return 0
            if not found:
                counts = 0
                for group in groups:
                    counts += (len(group)-contigs[0]+1)
                # print(f'group: {group}, contig: {contigs[0]} - valid!')
                return counts
            # Otherwise, find group that has the pound
            group = list(filter(lambda l: '#' in l, groups))[0]
            contig = contigs[0]
            counts = 0
            pos = (''.join(group)).find('#')
            for start_pos in range(0, min(len(group)-contig+1, pos+1)):
                end_pos = start_pos + contig
                if len(group) > 1:
                    if start_pos > 0 and group[start_pos-1] == '#':
                        # print(f'group: {group}, contig: {contig}, startpos {start_pos} - invalid')
                        continue
                    if end_pos < len(group) and group[end_pos] == '#':
                        # print(f'group: {group}, contig: {contig}, startpos {start_pos} - invalid')
                        continue
                # print(f'group: {group}, contig: {contig}, startpos {start_pos} - valid!')
                counts += 1
            return counts
        
        counts = 0
        for group_idx, group in enumerate(groups):
            # group = groups[0]
            contig = contigs[0]
            pos = sys.maxsize if (''.join(group)).find('#') == -1 else (''.join(group)).find('#')+1
            # Loop through each possible starting position
            for start_pos in range(0, min(len(group)-contig+1, pos)):
                # print(f'group: {group}, contig: {contig}, startpos: {start_pos}')
                end_pos = start_pos + contig
                if len(group) > 1:
                    if start_pos > 0 and group[start_pos-1] == '#':
                        # print('Start pos makes  it invalid')
                        continue
                    if end_pos < len(group) and group[end_pos] == '#':
                        # print('end pos makes it invalid')
                        continue
                # print('Its valid!')
                # If valid, then recurse
                # check if we can break up the line
                # new_groups = groups.copy()[1:]
                new_groups = groups.copy()[group_idx+1:]
                if end_pos < len(group) - 1:
                    add_this = group[end_pos+1:]
                    new_groups.insert(0, add_this)
                thing = self.helper(new_groups, contigs[1:])
                # print(f'Recursion returned {thing}')
                counts += thing
            if '#' in group:
                break
        
        return counts



    def solve_puzzle(self):
        counts = 0
        counter = 1
        for l, c in [(x.strip().split(' ')[0], \
         list(map(int, x.strip().split(' ')[1].split(',')))) \
         for x in sys.stdin.readlines()]:
            print(f'On line {counter}')
            counter += 1

            line = ''
            contigs = list()
            for _ in range(4):
                line += (l + '?')
                contigs += c
            contigs += c
            line += l

            # line = l.strip()
            # contigs = c.copy()

            # Split line by periods
            groups = list(filter(lambda l: l != '', line.split('.')))
            # print(groups, contigs)
            test = self.helper(groups, contigs)
            # print(f'answer to this line is {test}')
            counts += test

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