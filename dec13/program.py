import sys

class Puzzle1():

    def find_split(self, grid: list) -> int:
        valid_split = -1
        for split in range(0, len(grid)-1):
            r1 = grid[:split+1]
            r1.reverse()
            r2 = grid[split+1:]
            to_check = min(len(r1), len(r2))
            valid_reflection = True
            for idx in range(0, to_check):
                if r1[idx] != r2[idx]:
                    valid_reflection = False
                    break
            if valid_reflection:
                valid_split = split
                break
        if valid_split >= 0:
            return valid_split+1
        return -1

    def solve_puzzle(self):
        lines = sys.stdin.read().split('\n\n')
        ans = 0
        for line in lines:
            grid = [list(l) for l in line.split('\n')]
            ref = self.find_split(grid)
            if ref >= 0:
                ans += (ref*100)
                continue
            new_grid =[[row[i] for row in grid] for i in range(len(grid[0]))]
            ref = self.find_split(new_grid)
            if ref >= 0:
                ans += ref
        print(f'The answer to puzzle 1 is {ans}')



def puzzle2():
    pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
        SOL.solve_puzzle()
    elif sys.argv[1] == '2':
        puzzle2()