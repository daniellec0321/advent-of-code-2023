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
        return (t[0]*n, t[1]*n)
    
    def addt(self, a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
        return (a[0]+b[0], a[1]+b[1])

    def solve_puzzle(self, stream=sys.stdin):

        # Create the grid
        grid = list()
        start_spot = (0,0)
        dir, to_move, _ = stream.readline().split(' ')
        if dir == 'L' or dir == 'R':
            grid = [['-'] * (int(to_move)+1)]
        else:
            grid = [['|']] * (int(to_move)+1)
        if dir == 'R':
            start_spot = (0, int(to_move))
        elif dir == 'D':
            start_spot = (int(to_move), 0)
        print(grid)

        # Read through grid
        curr_spot = start_spot
        curr_dir = dir
        for dir, a, _ in [x.strip().split(' ') for x in stream.readlines()]:
            to_move = int(a)

            # Write the direction change
            print(curr_spot)
            grid[curr_spot[0]][curr_spot[1]] = self.direction_change[(curr_dir, dir)]

            # Check where the ending spot will be
            end_spot = self.addt(curr_spot, self.multt(self.direction_move[dir], to_move))



class Puzzle2():
    def solve_puzzle(self, stream=sys.stdin):
        pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()