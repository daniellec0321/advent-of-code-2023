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



def puzzle2():
    pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()