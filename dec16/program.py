import sys
from queue import Queue

class Puzzle1():

    def solve_puzzle(self, stream=sys.stdin):
        # Read in grid
        self.grid = [list(x.strip()) for x in stream.readlines()]
        self.dp = set() # tuples with coordinates, direction
        self.energized = set() # a set of coordinates that are energized
        self.directions = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}
        self.run_beam((0,0), 'right')
        print(f'The answer to puzzle 1 is {len(self.energized)}')

    def addt(self, t1, t2):
        return tuple([sum(x) for x in zip(t1, t2)])

    def run_beam(self, start_location: tuple[int, int], start_direction: str):

        # Add this to the queue
        q = Queue()
        q.put((start_location, start_direction))

        while not q.empty():

            # Pop from the queue
            spot, direction = q.get()
            x, y = spot
            
            # Check if in range or in dp
            if not (0 <= x < len(self.grid)) or not (0 <= y < len(self.grid[0])):
                continue
            if (spot, direction) in self.dp:
                continue

            # add to energized and dp
            self.energized.add(spot)
            self.dp.add((spot, direction))

            char = self.grid[x][y]

            # Go through cases
            if char == '|' and ((direction == 'left') or (direction == 'right')):
                up_spot = self.addt(spot, self.directions['up'])
                down_spot = self.addt(spot, self.directions['down'])
                q.put((up_spot, 'up'))
                q.put((down_spot, 'down'))
            elif char == '-' and ((direction == 'up') or (direction == 'down')):
                left_spot = self.addt(spot, self.directions['left'])
                right_spot = self.addt(spot, self.directions['right'])
                q.put((right_spot, 'right'))
                q.put((left_spot, 'left'))
            elif char == '/':
                if direction == 'right':
                    new_spot = self.addt(spot, self.directions['up'])
                    q.put((new_spot, 'up'))
                elif direction == 'left':
                    new_spot = self.addt(spot, self.directions['down'])
                    q.put((new_spot, 'down'))
                elif direction == 'up':
                    new_spot = self.addt(spot, self.directions['right'])
                    q.put((new_spot, 'right'))
                else:
                    new_spot = self.addt(spot, self.directions['left'])
                    q.put((new_spot, 'left'))
            elif char == '\\':
                if direction == 'right':
                    new_spot = self.addt(spot, self.directions['down'])
                    q.put((new_spot, 'down'))
                elif direction == 'left':
                    new_spot = self.addt(spot, self.directions['up'])
                    q.put((new_spot, 'up'))
                elif direction == 'up':
                    new_spot = self.addt(spot, self.directions['left'])
                    q.put((new_spot, 'left'))
                else:
                    new_spot = self.addt(spot, self.directions['right'])
                    q.put((new_spot, 'right'))
            else:
                new_spot = self.addt(spot, self.directions[direction])
                q.put((new_spot, direction))

class Puzzle2():

    def solve_puzzle(self, stream=sys.stdin):
        # Read in grid
        self.grid = [list(x.strip()) for x in stream.readlines()]
        self.directions = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}
        # Find all start locations on edges
        edge_locations = [(i,j) for j in range(len(self.grid[0])) \
         for i in range(len(self.grid)) if i == 0 or j == 0 or i == len(self.grid)-1 or j == len(self.grid[0])-1]
        max_energy = -1
        print(f'Tests to run: {len(edge_locations)}')
        for idx, start_location in enumerate(edge_locations):
            print(f'Test {idx}')
            x, y = start_location
            if x == 0:
                max_energy = max(max_energy, self.run_beam(start_location, 'down'))
            if x == len(self.grid)-1:
                max_energy = max(max_energy, self.run_beam(start_location, 'up'))
            if y == 0:
                max_energy = max(max_energy, self.run_beam(start_location, 'right'))
            if y == len(self.grid[0])-1:
                max_energy = max(max_energy, self.run_beam(start_location, 'left'))
        print(f'The answer to puzzle 2 is {max_energy}')

    def addt(self, t1, t2):
        return tuple([sum(x) for x in zip(t1, t2)])

    def run_beam(self, start_location: tuple[int, int], start_direction: str) -> int:

        dp = set()
        energized = set()

        # Add this to the queue
        q = Queue()
        q.put((start_location, start_direction))

        while not q.empty():

            # Pop from the queue
            spot, direction = q.get()
            x, y = spot
            
            # Check if in range or in dp
            if not (0 <= x < len(self.grid)) or not (0 <= y < len(self.grid[0])):
                continue
            if (spot, direction) in dp:
                continue

            # add to energized and dp
            energized.add(spot)
            dp.add((spot, direction))

            char = self.grid[x][y]

            # Go through cases
            if char == '|' and ((direction == 'left') or (direction == 'right')):
                up_spot = self.addt(spot, self.directions['up'])
                down_spot = self.addt(spot, self.directions['down'])
                q.put((up_spot, 'up'))
                q.put((down_spot, 'down'))
            elif char == '-' and ((direction == 'up') or (direction == 'down')):
                left_spot = self.addt(spot, self.directions['left'])
                right_spot = self.addt(spot, self.directions['right'])
                q.put((right_spot, 'right'))
                q.put((left_spot, 'left'))
            elif char == '/':
                if direction == 'right':
                    new_spot = self.addt(spot, self.directions['up'])
                    q.put((new_spot, 'up'))
                elif direction == 'left':
                    new_spot = self.addt(spot, self.directions['down'])
                    q.put((new_spot, 'down'))
                elif direction == 'up':
                    new_spot = self.addt(spot, self.directions['right'])
                    q.put((new_spot, 'right'))
                else:
                    new_spot = self.addt(spot, self.directions['left'])
                    q.put((new_spot, 'left'))
            elif char == '\\':
                if direction == 'right':
                    new_spot = self.addt(spot, self.directions['down'])
                    q.put((new_spot, 'down'))
                elif direction == 'left':
                    new_spot = self.addt(spot, self.directions['up'])
                    q.put((new_spot, 'up'))
                elif direction == 'up':
                    new_spot = self.addt(spot, self.directions['left'])
                    q.put((new_spot, 'left'))
                else:
                    new_spot = self.addt(spot, self.directions['right'])
                    q.put((new_spot, 'right'))
            else:
                new_spot = self.addt(spot, self.directions[direction])
                q.put((new_spot, direction))

        return len(energized)



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()