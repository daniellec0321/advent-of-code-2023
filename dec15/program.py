import sys

class Puzzle1():

    def solve_puzzle(self, stream=sys.stdin):
        sum = 0
        for elem in sys.stdin.readline().strip().split(','):
            current_value = 0
            for char in elem:
                current_value += ord(char)
                current_value *= 17
                current_value %= 256
            sum += current_value
        print(f'The answer to puzzle 1 is {sum}')



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