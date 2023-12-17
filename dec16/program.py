import sys

class Puzzle1():

    def solve_puzzle(self, stream=sys.stdin):
        # Read in grid
        self.grid = [list(x.strip()) for x in stream.readlines()]
        self.dp = set() # tuples with coordinates, direction
        self.energized = set() # a set of coordinates that are energized
        self.run_beam((0,0), 'right')

    def run_beam(self, start_location: tuple[int, int], direction: str):
        # Check if this beam has already been run
        if (start_location, direction) in self.dp:
            return
        
        # add this start location to energized
        self.energized.add(start_location)
        
        # Get list of where the beam is going
        track = list()
        if direction == 'right':
            track = self.grid[start_location[0]][start_location[1]+1:]
        elif direction == 'left':
            track = self.grid[start_location[0]][:start_location[1]]
            track.reverse()
        elif direction == 'down':
            pass



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