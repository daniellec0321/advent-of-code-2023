import sys

class Puzzle1():

    def solve_puzzle(self, stream=sys.stdin):
        # Read in grid
        self.grid = [list(x.strip()) for x in stream.readlines()]
        self.dp = set() # tuples with coordinates, direction
        self.energized = set() # a set of coordinates that are energized
        self.directions = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}
        self.run_beam((0,0), 'right')
        # test = list(self.energized)
        # test = sorted(test)
        # for elem in test:
        #     print(elem)
        print(f'The answer to puzzle 1 is {len(self.energized)}')

    def addt(self, t1, t2):
        return tuple([sum(x) for x in zip(t1, t2)])

    def run_beam(self, start_location: tuple[int, int], direction: str):

        # Check if beam out of range
        if start_location[0] < 0 or start_location[1] < 0 or \
        start_location[0] >= len(self.grid) or start_location[1] >= len(self.grid[0]):
            return
        
        print(start_location, direction)

        # Check if this beam has already been run
        if (start_location, direction) in self.dp:
            return
        
        # add this start location to energized and dp
        self.energized.add(start_location)
        self.dp.add((start_location, direction))

        # get locations to recurse to
        char = self.grid[start_location[0]][start_location[1]]

        if char == '|' and ((direction == 'left') or (direction == 'right')):
            self.run_beam(self.addt(start_location, self.directions['up']), 'up')
            self.run_beam(self.addt(start_location, self.directions['down']), 'down')
        elif char == '-' and ((direction == 'down') or (direction == 'up')):
            self.run_beam(self.addt(start_location, self.directions['right']), 'right')
            self.run_beam(self.addt(start_location, self.directions['left']), 'left')
        elif char == '/':
            if direction == 'up':
                self.run_beam(self.addt(start_location, self.directions['right']), 'right')
            elif direction == 'down':
                self.run_beam(self.addt(start_location, self.directions['left']), 'left')
            elif direction == 'left':
                self.run_beam(self.addt(start_location, self.directions['down']), 'down')
            else:
                self.run_beam(self.addt(start_location, self.directions['up']), 'up')
        elif char == '\\':
            if direction == 'up':
                self.run_beam(self.addt(start_location, self.directions['left']), 'left')
            elif direction == 'down':
                self.run_beam(self.addt(start_location, self.directions['right']), 'right')
            elif direction == 'left':
                self.run_beam(self.addt(start_location, self.directions['up']), 'up')
            else:
                self.run_beam(self.addt(start_location, self.directions['down']), 'down')
        else:
            # to_go.append(self.addt(start_location, self.directions[direction]))
            self.run_beam(self.addt(start_location, self.directions[direction]), direction)

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