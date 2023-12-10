import sys

def puzzle1():
    directions = list(sys.stdin.readline().rstrip())
    graph = dict() # Key: string representing location. Value: tuple of its left and right
    for line in [x.rstrip() for x in sys.stdin.readlines() if x != '\n']:
        location = line.split('=')[0].strip()
        left = line.split('=')[1].split('(')[1].split(',')[0].strip()
        right = line.split('=')[1].split('(')[1].split(',')[1].split(')')[0].strip()
        graph[location] = (left, right)
    current_location = 'AAA'
    num_moves = 0
    while current_location != 'ZZZ':
        for turn in directions:
            if current_location == 'ZZZ':
                break
            if turn == 'L':
                current_location = graph[current_location][0]
            else:
                current_location = graph[current_location][1]
            num_moves += 1
    print(f'The answer to puzzle 1 is {num_moves}')



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