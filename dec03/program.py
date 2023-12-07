import re

def get_digits(line: str) -> dict: # Key: index in the line, value: the number

    ret = dict()
    it = 0

    while it < len(line):
        curr_substring = ''
        if line[it].isdigit():
            curr_index = it
            curr_substring += line[it]
            it += 1
            while (it < len(line)) and (line[it].isdigit()):
                curr_substring += line[it]
                it += 1
            # Add on to ret
            ret[curr_index] = curr_substring
            curr_substring = ''
        it += 1

    return ret



if __name__ == '__main__':
    
    # Puzzle 1
    f = open('input.txt', 'r')

    # Making the puzzle grid (also making a buffer)
    grid = [x.strip() for x in f.readlines()]
    grid = [''.join('.' for _ in grid[0])] + grid + [''.join('.' for _ in grid[0])]
    grid = ['.' + line + '.' for line in grid]
    sum = 0

    # Check each line in the puzzle grid
    for col, line in enumerate(grid):
        nums_dict = get_digits(line.rstrip())
        if len(nums_dict) == 0:
            continue

        # Loop through indices
        for index, curr_num in nums_dict.items():
            # Get all of the tuples
            tuples = []
            for i in range(-1, len(curr_num)+1):
                tuples += [(col-1,index+i), (col,index+i), (col+1,index+i)]
            symbol_exists = False
            for t in tuples:
                if (not grid[t[0]][t[1]].isdigit()) and (grid[t[0]][t[1]] != '.'):
                    symbol_exists = True
                    break
            if symbol_exists:
                sum += int(curr_num)

    f.close()
    print(f'The answer to question 1 is {sum}')