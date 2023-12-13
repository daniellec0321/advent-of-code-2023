import sys

def puzzle1():
    old_grid = [list(line.strip()) for line in sys.stdin.readlines()]
    grid = []
    for line in old_grid:
        grid.append(line)
        if '#' not in line:
            grid.append(line)
    cols_to_add = [col_idx for col_idx in range(len(grid[0])) if '#' not in [line[col_idx] for line in grid]]
    for adder, idx in enumerate(cols_to_add):
        for row in range(len(grid)):
            print(f'Inserting period at row {row} index {idx+adder}')
            grid[row].insert(idx+adder, '.')
    for line in grid:
        print(line)



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