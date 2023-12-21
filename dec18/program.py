import sys

class Puzzle1():

    def __init__(self):
        self.direction_symbol = {'L': '-', 'R': '-', 'U': '|', 'D': '|'}
        self.direction_change = {('L', 'U'): 'L', ('L', 'D'): 'F', \
                                 ('R', 'U'): 'J', ('R', 'D'): '7', \
                                 ('U', 'L'): '7', ('U', 'R'): 'F', \
                                 ('D', 'L'): 'J', ('D', 'R'): 'L'}
        self.direction_move = {'L': (0,-1), 'R': (0,1), 'U': (-1,0), 'D': (1,0)}

    def multt(self, t: tuple[int, int], n: int) -> tuple[int, int]:
        ret = (t[0]*n, t[1]*n)
        return (t[0]*n, t[1]*n)
    
    def addt(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return (a[0]+b[0], a[1]+b[1])

    def solve_puzzle(self, stream=sys.stdin):

        # Create the grid
        grid = list()
        start_spot = (0,0)
        start_dir, to_move, _ = stream.readline().split(' ')
        if start_dir == 'L' or start_dir == 'R':
            grid = [['-'] * (int(to_move)+1)]
        else:
            grid = [['|']] * (int(to_move)+1)
        if start_dir == 'R':
            start_spot = (0, int(to_move))
        elif start_dir == 'D':
            start_spot = (int(to_move), 0)

        # Read through grid
        total_lava = int(to_move)
        curr_spot = start_spot
        curr_dir = start_dir
        for dir, a, _ in [x.strip().split(' ') for x in stream.readlines()]:
            # Write the direction change
            to_move = int(a)
            total_lava += to_move
            grid[curr_spot[0]][curr_spot[1]] = self.direction_change[(curr_dir, dir)]

            # Check where the ending spot will be
            end_spot = self.addt(curr_spot, self.multt(self.direction_move[dir], to_move))
            x, y = end_spot

            if (x < 0):
                # END SPOT AND CURR SPOT MOVES!!!!
                row_to_add = ['.'] * len(grid[0])
                for _ in range(abs(x)):
                    grid.insert(0, row_to_add.copy())
                end_spot = (0, end_spot[1])
                curr_spot = (curr_spot[0]+abs(x), curr_spot[1])

            if (x >= len(grid)):
                row_to_add = ['.'] * len(grid[0])
                for _ in range(x - len(grid) + 1):
                    grid.append(row_to_add.copy())

            # Check if y is in bounds
            if (y < 0):
                for line in grid:
                    for _ in range(abs(y)):
                        line.insert(0, '.')
                end_spot = (end_spot[0], 0)
                curr_spot = (curr_spot[0], curr_spot[1]+abs(y))

            if (y >= len(grid[0])):
                for line in grid:
                    for _ in range(abs(y)):
                        line.append('.')

            # Mark those spots on the grid
            curr_spot = self.addt(curr_spot, self.direction_move[dir])
            while curr_spot != end_spot:
                grid[curr_spot[0]][curr_spot[1]] = self.direction_symbol[dir]
                curr_spot = self.addt(curr_spot, self.direction_move[dir])

            # Update values
            curr_dir = dir

        # Add the last end spot (use start dir and curr dir)
        grid[curr_spot[0]][curr_spot[1]] = self.direction_change[(curr_dir, start_dir)]

        # Read through grid again, counting up the insides
        last_wall = '|'
        inside = False
        for line in grid:
            for char in line:
                if char == '|' or ((char == '7' and last_wall == 'L') or (char == 'J' and last_wall == 'F')):
                    inside = not inside
                    last_wall = '|'
                elif char == '7' or char == 'L' or char == 'F' or char == 'J':
                    last_wall = char
                elif char == '.' and inside:
                    total_lava += 1

        print(f'The answer to puzzle 1 is {total_lava}')



class Puzzle2():

    def __init__(self):
        # R: 0, D: 1, L: 2, U: 3
        self.direction_move = {'0': (0,1), '1': (1,0), '2': (0,-1), '3': (-1,0)}
        self.direction_change = {('2', '3'): 'L', ('2', '1'): 'F', \
                                 ('0', '3'): 'J', ('0', '1'): '7', \
                                 ('3', '2'): '7', ('3', '0'): 'F', \
                                 ('1', '2'): 'J', ('1', '0'): 'L'}
        self.rows = dict() # Key: The row. Value: a list of tuples (column, symbol)
        self.columns = dict() # Key: The column. Value: a list of tuples (row, symbol)
        
    def multt(self, t: tuple[int, int], n: int) -> tuple[int, int]:
        return (t[0]*n, t[1]*n)
        
    def addt(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return (a[0]+b[0], a[1]+b[1])

    def solve_puzzle(self, stream=sys.stdin):
        # First, read through all the instructions to find the total size of the grid.
        curr_spot = (0, 0)
        prev_dir = '0'
        first_dir = ''
        for symbol in [x.split(' ')[2].strip()[2:-1] for x in stream.readlines()]:
            to_move = int(symbol[:-1], 16)
            dir = symbol[-1]

            # Can update curr spot's direction change
            x, y = curr_spot
            if x not in self.rows:
                self.rows[x] = list()
            if y not in self.columns:
                self.columns[y] = list()
            if first_dir:
                self.rows[x].append((y, self.direction_change[(prev_dir, dir)]))
                self.columns[y].append((x, self.direction_change[(prev_dir, dir)]))
            else:
                first_dir = dir

            # Update all of the values
            curr_spot = self.addt(curr_spot, self.multt(self.direction_move[dir], to_move))
            prev_dir = dir
        
        # Update the first spot
        if 0 not in self.rows:
            self.rows[0] = list()
        if 0 not in self.columns:
            self.columns[0] = list()
        self.rows[0].append((0, self.direction_change[(dir, first_dir)]))
        self.columns[0].append((0, self.direction_change[(dir, first_dir)]))
        for key, value in self.rows.items():
            self.rows[key] = sorted(value)
        for key, value in self.columns.items():
            self.columns[key] = sorted(value)

        # Sort the row keys
        sorted_row_keys = sorted(self.rows.keys())
        sorted_column_keys = sorted(self.columns.keys())

        total_lava = 0
        # Process up and left, keep out right and bottom (unless at the end)
        for idx, row in enumerate(sorted_row_keys):
            # Find earliest column whose direction changes includes that row
            col1 = None
            col2 = None
            for col in sorted_column_keys:
                # Check all of its direction changes
                for i in range(len(self.columns[col])-1):
                    curr1 = self.columns[col][i][0]
                    curr2 = self.columns[col][i+1][0]
                    if (curr1 <= row <= curr2):
                        print('found something')
                        print(f'row: {row}, col: {col}, curr1: {curr1}, curr2: {curr2}\n')
                        if col1 == None:
                            col1 = col
                        elif col2 == None:
                            col2 = col
                            break
                if (col1 != None) and (col2 != None):
                    break
            print(f'For row {row}, found {col1} and {col2}')
            


if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()