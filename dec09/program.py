import sys

def puzzle1():
    # Recursive function that takes an array and returns the next rightmost element
    def helper(arr: list[int]) -> int:
        # Base case: The array is all zeroes
        if len(list(filter(lambda l: l != 0, arr))) == 0:
            return 0
        # Otherwise, find sequence of differences and recurse
        diff = [arr[i+1]-arr[i] for i in range(0, len(arr)-1)]
        add_on = helper(diff)
        return arr[-1] + add_on

    ans = 0
    for line in [list(map(int, x.strip().split(' '))) for x in sys.stdin.readlines()]:
        ans += helper(line)
    print(f'The answer to puzzle 1 is {ans}')



def puzzle2():
    # Recursive function that takes an array and returns the next rightmost element
    def helper(arr: list[int]) -> int:
        # Base case: The array is all zeroes
        if len(list(filter(lambda l: l != 0, arr))) == 0:
            return 0
        # Otherwise, find sequence of differences and recurse
        diff = [arr[i+1]-arr[i] for i in range(0, len(arr)-1)]
        add_on = helper(diff)
        return arr[0] - add_on

    ans = 0
    for line in [list(map(int, x.strip().split(' '))) for x in sys.stdin.readlines()]:
        ans += helper(line)
    print(f'The answer to puzzle 1 is {ans}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()