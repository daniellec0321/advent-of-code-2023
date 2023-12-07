import sys

def puzzle1():
    sum = 0
    for line in [x.rstrip().split(':')[1].rstrip() for x in sys.stdin.readlines()]:
        winning_nums = set([x for x in line.split('|')[0].split(' ') if x != ''])
        my_nums = set([x for x in line.split('|')[1].split(' ') if x != ''])
        u = set.intersection(winning_nums, my_nums)
        prod = pow(2, len(u)-1) if pow(2, len(u)-1) >= 1 else 0
        sum += prod
    print(f'The answer to puzzle 1 is {sum}')

def puzzle2():
    inp = sys.stdin.read()

if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    else:
        puzzle2()