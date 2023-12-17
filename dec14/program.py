import sys
from collections import Counter

class Puzzle1():

    def roll_north(self, grid: list[str]) -> list[str]:
        transposed_grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
        for idx, line in enumerate(transposed_grid):
            new_line = ''
            next_section = ''.join(line)
            while next_section:
                curr_section, delim, next_section = next_section.partition('#')
                if curr_section:
                    c = Counter(list(curr_section))
                    new_line += ('O' * c['O'])
                    new_line += ('.' * (len(curr_section)-c['O']))
                if delim:
                    new_line += '#'
            transposed_grid[idx] = new_line
        # Retranspose grid and return
        rolled_grid = [[row[i] for row in transposed_grid] for i in range(len(transposed_grid[0]))]
        for idx, line in enumerate(rolled_grid):
            rolled_grid[idx] = ''.join(line)
        return rolled_grid

    def solve_puzzle(self, stream=sys.stdin):
        grid = [x.strip() for x in stream]
        rolled_grid = self.roll_north(grid)
        total_weight = 0
        for idx, line in enumerate(rolled_grid):
            num_rocks = Counter(line)['O']
            factor = len(rolled_grid) - idx
            total_weight += (num_rocks * factor)
        print(f'The answer to puzzle 1 is {total_weight}')



class Puzzle2():

    def roll(self, grid: list[list[str]]) -> list[list[str]]:
        new_grid = grid.copy()
        for idx, line in enumerate(grid):
            new_line = ''
            next_section = ''.join(line)
            while next_section:
                curr_section, delim, next_section = next_section.partition('#')
                if curr_section:
                    c = Counter(list(curr_section))
                    new_line += ('O' * c['O'])
                    new_line += ('.' * (len(curr_section)-c['O']))
                if delim:
                    new_line += '#'
            new_grid[idx] = new_line
        return new_grid
    
    def roll_north(self, grid: list[list[str]]) -> list[list[str]]:
        transposed_grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
        rolled_grid = self.roll(transposed_grid)
        ret = [[row[i] for row in rolled_grid] for i in range(len(rolled_grid[0]))]
        return ret

    def roll_south(self, grid: list[list[str]]) -> list[list[str]]:
        transposed_grid = [[row[i] for row in grid] for i in range(len(grid[0]))]
        mirrored_grid = [[row[len(row)-i-1] for i in range(len(row))] for row in transposed_grid]
        rolled_grid = self.roll(mirrored_grid)
        ret = [[row[len(row)-i-1] for i in range(len(row))] for row in rolled_grid]
        ret = [[row[i] for row in ret] for i in range(len(ret[0]))]
        return ret

    def roll_west(self, grid: list[list[str]]) -> list[list[str]]:
        ret = self.roll(grid)
        return ret

    def roll_east(self, grid: list[list[str]]) -> list[list[str]]:
        mirrored_grid = [[row[len(row)-i-1] for i in range(len(row))] for row in grid]
        rolled_grid = self.roll(mirrored_grid)
        ret = [[row[len(row)-i-1] for i in range(len(row))] for row in rolled_grid]
        return ret

    def solve_puzzle(self, stream=sys.stdin):
        grid = [list(x.strip()) for x in stream]

        

        total_weight = 0
        print(f'The answer to puzzle 2 is {total_weight}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()