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

    def find_spot(start_index: tuple, came_from: tuple) -> tuple:
        moves = {'north': (-1,0,), 'east': (0,1), 'south': (1,0), 'west': (0,-1)}
        for move, coord in moves.items():
            spot = tuple(np.add(start_index, coord))
            # Check that coord is in grid
            if (spot == came_from) or (spot[0] < 0) or (spot[1] < 0) or (spot[0] >= len(grid)) or (spot[1] >= len(grid[0])):
                continue
            # Check if this is a valid connection
            symbol = grid[spot[0]][spot[1]]
            if (move == 'north' and ((symbol == '|') or (symbol == '7') or (symbol == 'F'))) or \
                (move == 'east' and ((symbol == '-') or (symbol == '7') or (symbol == 'J'))) or \
                (move == 'south' and ((symbol == '|') or (symbol == 'J') or (symbol == 'L'))) or \
                (move == 'west' and ((symbol == '-') or (symbol == 'L') or (symbol == 'F'))):
                return spot
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
    s1_visited = {s1}
    s2_visited = {s2}
    s1_came_from = start_index
    s2_came_from = start_index
    while len(set.intersection(s1_visited, s2_visited)) == 0:
        # print(s1, s2)
        # s1, s2 = find_spots(start_index)
        s1 = find_spot()
        s1_visited.add(s1)
        s2_visited.add(s2)
        total_moves += 1
    print(total_moves)



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