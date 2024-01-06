import sys
from queue import Queue

class Puzzle1():

    def addt(t1: tuple, t2: tuple) -> tuple:
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
        visited.add((*start_point, 0))

        moves = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while not frontier.empty:
            x, y, curr_cycle = frontier.get()
            if curr_cycle == 64:
                end_spots.add((x, y))
                continue
            # Add on possible spots to queue



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