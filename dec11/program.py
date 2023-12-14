import sys

def puzzle1():
    old_grid = [list(line.strip()) for line in sys.stdin.readlines()]
    grid = []
    for line in old_grid:
        grid.append(line.copy())
        if '#' not in line:
            grid.append(line.copy())
    cols_to_add = [col_idx for col_idx in range(len(grid[0])) if '#' not in [line[col_idx] for line in grid]]
    for adder, idx in enumerate(cols_to_add):
        for line in grid:
            line.insert(idx+adder, '.')
    # Loop through sets and find the distances
    galaxies = [(row,col) for row, line in enumerate(grid) for col, symbol in enumerate(line) if symbol == '#']
    total_distance = 0
    while galaxies:
        curr = galaxies.pop()
        for galaxy in galaxies:
            total_distance += (abs(curr[0]-galaxy[0]) + abs(curr[1]-galaxy[1]))
    print(f'The answer to puzzle 1 is {total_distance}')



def puzzle2():
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    galaxies = [(row,col) for row, line in enumerate(grid) for col, symbol in enumerate(line) if symbol == '#']
    moved_positions = dict()
    for row, col in galaxies:
        moved_positions[(row,col)] = (row,col)
    # Find empty rows
    for row, line in enumerate(grid):
        if '#' not in line:
            for r, c in moved_positions.keys():
                if r > row:
                    moved_positions[(r,c)] = (moved_positions[(r,c)][0]+999999, moved_positions[(r,c)][1])
    # Find empty columns
    cols = [[row[i] for row in grid] for i in range(len(grid[0]))]
    for col, line in enumerate(cols):
        if '#' not in line:
            for r, c in moved_positions.keys():
                if c > col:
                    moved_positions[(r,c)] = (moved_positions[(r,c)][0], moved_positions[(r,c)][1]+999999)
    # Loop through sets and find the distances
    galaxies_to_find = list(moved_positions.values())
    total_distance = 0
    while galaxies_to_find:
        curr = galaxies_to_find.pop()
        for galaxy in galaxies_to_find:
            total_distance += (abs(curr[0]-galaxy[0]) + abs(curr[1]-galaxy[1]))
    print(f'The answer to puzzle 2 is {total_distance}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()