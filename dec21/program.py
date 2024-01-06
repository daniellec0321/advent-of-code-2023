import sys
from queue import Queue

class Puzzle1():

    def addt(self, t1: tuple, t2: tuple) -> tuple:
        return tuple([sum(x) for x in zip(t1, t2)])

    def solve_puzzle(self, stream=sys.stdin):
        # Read in map
        grid = list()
        for idx, line in enumerate(stream.readlines()):
            grid.append(line.strip())
            if 'S' in line:
                start_point = (idx, line.find('S'))

        frontier = Queue() # tuples of (x, y, cycle)
        visited = set() # tuples of (x, y, cycle)
        end_spots = set() # tuples of (x, y)
        frontier.put((*start_point, 0))

        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        x_lim = len(grid)
        y_lim = len(grid[0])
        
        while not frontier.empty():
            x, y, curr_cycle = frontier.get()
            if curr_cycle == 64:
                end_spots.add((x, y))
                continue
            if (x, y, curr_cycle) in visited:
                continue
            visited.add((x, y, curr_cycle))
            # Add on possible spots to queue
            togo = [self.addt((x,y), m) for m in moves]
            togo = [elem for elem in togo if (0 <= elem[0] < x_lim) and \
                    (0 <= elem[1] < y_lim) and grid[elem[0]][elem[1]] != '#']
            for m in togo:
                frontier.put((*m, curr_cycle+1))

        # print(end_spots)
        print(f'The answer to puzzle 1 is {len(end_spots)}')




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