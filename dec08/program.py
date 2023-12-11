import sys
from math import lcm
from itertools import product

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

    directions = list(sys.stdin.readline().rstrip())
    graph = dict() # Key: string representing location. Value: tuple of its left and right
    a_nodes = list()
    z_nodes = list()
    for line in [x.rstrip() for x in sys.stdin.readlines() if x != '\n']:
        location = line.split('=')[0].strip()
        left = line.split('=')[1].split('(')[1].split(',')[0].strip()
        right = line.split('=')[1].split('(')[1].split(',')[1].split(')')[0].strip()
        graph[location] = (left, right)
        if location[-1] == 'A':
            a_nodes.append(location)
        if location[-1] == 'Z':
            z_nodes.append(location)

    possible_moves = dict()
    for start_location in a_nodes:
        moves = set()
        for end_location in z_nodes:
            current_location = start_location
            num_moves = 0
            dp = set()
            break_outer = False
            while current_location != end_location:
                for turn_idx, turn in enumerate(directions):
                    # Add current location to dp
                    if current_location == end_location:
                        break_outer = True
                        break
                    if (turn_idx, current_location) in dp:
                        num_moves = -1
                        break_outer = True
                        break
                    dp.add((turn_idx, current_location))
                    if turn == 'L':
                        current_location = graph[current_location][0]
                    else:
                        current_location = graph[current_location][1]
                    num_moves += 1
                if break_outer:
                    break
            if num_moves != -1:
                moves.add(num_moves)
        possible_moves[start_location] = moves
    # print(possible_moves)



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()