import sys
import numpy as np

def puzzle1():

    # helper function that finds a spot
    def find_initial_spots(start_index: tuple) -> tuple:
        s1 = start_index
        s2 = start_index
        moves = {'north': (-1,0,), 'east': (0,1), 'south': (1,0), 'west': (0,-1)}
        for move, coord in moves.items():
            spot = tuple(np.add(start_index, coord))
            # Check that coord is in grid
            if (spot[0] < 0) or (spot[1] < 0) or (spot[0] >= len(grid)) or (spot[1] >= len(grid[0])):
                continue
            # Check if this is a valid connection
            symbol = grid[spot[0]][spot[1]]
            if (move == 'north' and ((symbol == '|') or (symbol == '7') or (symbol == 'F'))) or \
                (move == 'east' and ((symbol == '-') or (symbol == '7') or (symbol == 'J'))) or \
                (move == 'south' and ((symbol == '|') or (symbol == 'J') or (symbol == 'L'))) or \
                (move == 'west' and ((symbol == '-') or (symbol == 'L') or (symbol == 'F'))):
                if s1 == start_index:
                    s1 = spot
                else:
                    s2 = spot
                    break
        return (s1, s2)

    def find_spot(curr_index: tuple, came_from: tuple) -> tuple:
        symbol = grid[curr_index[0]][curr_index[1]]
        moves = []
        if symbol == '-':
            moves = [tuple(np.add(curr_index, (0,-1)))] + [tuple(np.add(curr_index, (0,1)))]
        elif symbol == '|':
            moves = [tuple(np.add(curr_index, (-1,0)))] + [tuple(np.add(curr_index, (1,0)))]
        elif symbol == 'L':
            moves = [tuple(np.add(curr_index, (-1,0)))] + [tuple(np.add(curr_index, (0,1)))]
        elif symbol == 'J':
            moves = [tuple(np.add(curr_index, (-1,0)))] + [tuple(np.add(curr_index, (0,-1)))]
        elif symbol == '7':
            moves = [tuple(np.add(curr_index, (1,0)))] + [tuple(np.add(curr_index, (0,-1)))]
        elif symbol == 'F':
            moves = [tuple(np.add(curr_index, (1,0)))] + [tuple(np.add(curr_index, (0,1)))]
        for move in moves:
            if move != came_from:
                return move
        return (-1, -1)

    # Read in grid
    grid = [line.strip() for line in sys.stdin.readlines()]
    # Find index of starting position
    start_index = (-1,-1)
    for row, line in enumerate(grid):
        spot = line.find('S')
        if spot != -1:
            start_index = (row, spot)
    # Initialize spots
    s1, s2 = find_initial_spots(start_index)
    total_moves = 1
    s1_came_from = start_index
    s2_came_from = start_index
    while s1 != s2:
        s1_new = find_spot(s1, s1_came_from)
        s2_new = find_spot(s2, s2_came_from)
        s1_came_from = s1
        s2_came_from = s2
        s1 = s1_new
        s2 = s2_new
        total_moves += 1
    
    print(f'The answer to puzzle 1 is {total_moves}')



def puzzle2():
    
    # helper function that finds a spot
    def find_initial_spots(start_index: tuple) -> tuple:
        s_symbols = {'|', '-', 'F', 'J', 'L', '7'}
        s1 = start_index
        s2 = start_index
        moves = {'north': (-1,0,), 'east': (0,1), 'south': (1,0), 'west': (0,-1)}
        for move, coord in moves.items():
            spot = tuple(np.add(start_index, coord))
            # Check that coord is in grid
            if (spot[0] < 0) or (spot[1] < 0) or (spot[0] >= len(grid)) or (spot[1] >= len(grid[0])):
                continue
            # Check if this is a valid connection
            symbol = grid[spot[0]][spot[1]]
            if (move == 'north' and ((symbol == '|') or (symbol == '7') or (symbol == 'F'))) or \
                (move == 'east' and ((symbol == '-') or (symbol == '7') or (symbol == 'J'))) or \
                (move == 'south' and ((symbol == '|') or (symbol == 'J') or (symbol == 'L'))) or \
                (move == 'west' and ((symbol == '-') or (symbol == 'L') or (symbol == 'F'))):
                # Set s symbol
                # if move == 'east' or move == 'west':
                #     s_symbols.discard('|')
                # if move == 'north' or move == 'south':
                #     s_symbols.discard('-')
                # if move == 'east' or move == 'south':
                #     s_symbols.discard('F')
                # if move == 'north' or move == 'west':
                #     s_symbols.discard('J')
                # if move == 'north' or move == 'east':
                #     s_symbols.discard('L')
                # if move == 'south' or move == 'west':
                #     s_symbols.discard('7')
                if move == 'north':
                    s_symbols.discard('-')
                    s_symbols.discard('7')
                    s_symbols.discard('F')
                elif move == 'south':
                    s_symbols.discard('-')
                    s_symbols.discard('J')
                    s_symbols.discard('L')
                elif move == 'east':
                    s_symbols.discard('|')
                    s_symbols.discard('J')
                    s_symbols.discard('7')
                else:
                    s_symbols.discard('|')
                    s_symbols.discard('F')
                    s_symbols.discard('L')
                if s1 == start_index:
                    s1 = spot
                else:
                    s2 = spot
                    break
        if len(s_symbols) != 1:
            print('what da hell')
            exit()
        return (s1, s2, list(s_symbols)[0])

    def find_spot(curr_index: tuple, came_from: tuple) -> tuple:
        symbol = grid[curr_index[0]][curr_index[1]]
        moves = []
        if symbol == '-':
            moves = [tuple(np.add(curr_index, (0,-1)))] + [tuple(np.add(curr_index, (0,1)))]
        elif symbol == '|':
            moves = [tuple(np.add(curr_index, (-1,0)))] + [tuple(np.add(curr_index, (1,0)))]
        elif symbol == 'L':
            moves = [tuple(np.add(curr_index, (-1,0)))] + [tuple(np.add(curr_index, (0,1)))]
        elif symbol == 'J':
            moves = [tuple(np.add(curr_index, (-1,0)))] + [tuple(np.add(curr_index, (0,-1)))]
        elif symbol == '7':
            moves = [tuple(np.add(curr_index, (1,0)))] + [tuple(np.add(curr_index, (0,-1)))]
        elif symbol == 'F':
            moves = [tuple(np.add(curr_index, (1,0)))] + [tuple(np.add(curr_index, (0,1)))]
        for move in moves:
            if move != came_from:
                return move
        return (-1, -1)

    # Read in grid
    grid = [line.strip() for line in sys.stdin.readlines()]
    route = dict()
    # Find index of starting position
    start_index = (-1,-1)
    for row, line in enumerate(grid):
        for idx, symbol in enumerate(line):
            if symbol == 'S':
                start_index = (row, idx)
                route[(row,idx)] = 'r'
            else:
                route[(row,idx)] = 'n'
    # Initialize spots (testing for the start of s)
    s1, s2, s_symbol = find_initial_spots(start_index)
    route[s1] = 'r'
    route[s2] = 'r'
    s1_came_from = start_index
    s2_came_from = start_index
    while s1 != s2:
        s1_new = find_spot(s1, s1_came_from)
        s2_new = find_spot(s2, s2_came_from)
        s1_came_from = s1
        s2_came_from = s2
        s1 = s1_new
        s2 = s2_new
        route[s1] = 'r'
        route[s2] = 'r'
    # Convert start symbol
    grid[start_index[0]] = list(grid[start_index[0]])
    grid[start_index[0]][start_index[1]] = s_symbol
    grid[start_index[0]] = ''.join(grid[start_index[0]])
    # Now that route is found, loop through grid to find inside
    inside_count = 0
    inside_flag = False
    last_wall = '|'
    for row, line in enumerate(grid):
        last_wall = '|'
        inside_flag = False
        for col, symbol in enumerate(line):
            if route[(row,col)] == 'r' and (symbol == '|' or \
                (symbol == '7' and last_wall == 'L') or \
                (symbol == 'J' and last_wall == 'F')):
                inside_flag = not inside_flag
                last_wall = symbol
            elif route[(row,col)] == 'r' and \
                (symbol == '7' or symbol == 'J' or symbol == 'L' or symbol == 'F'):
                last_wall = symbol
            elif inside_flag and route[(row,col)] != 'r':
                inside_count += 1

    print(f'The answer to puzzle 2 is {inside_count}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()