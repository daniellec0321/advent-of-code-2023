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
    pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()