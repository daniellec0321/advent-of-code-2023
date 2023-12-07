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

def find_nums(line: str, index: int, row_num: int) -> list: # given a line and index, returns the index of where that number starts and the number
    if not line[index].isdigit():
        return [(-1,-1), '']
    fixed_line = line.replace('*', '.')
    it = index
    while it > 0 and fixed_line[it].isdigit():
        it -= 1
    it += 1
    # print(f'found it to be {it}')
    num = fixed_line[it:].split('.')[0]
    return [(row_num, it), int(num)]



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
    
    # Puzzle 2
    f = open('test.txt', 'r')

    # Making the puzzle grid (also making a buffer)
    grid = [x.strip() for x in f.readlines()]
    grid = [''.join('.' for _ in grid[0])] + grid + [''.join('.' for _ in grid[0])]
    grid = ['.' + line + '.' for line in grid]
    # Clear all symbols on the grid if not '*' or a digit
    for row, line in enumerate(grid):
        grid[row] = list(line)
        for col, elem in enumerate(line):
            if (not elem.isdigit()) and (elem != '*'):
                grid[row][col] = '.'
        grid[row] = ''.join(grid[row])

    sum = 0

    for line in grid:
        thing = ''.join(line)
        print(line)

    for col, line in enumerate(grid):
        # Find if there is a star in the line
        occs = [i for i, letter in enumerate(line) if letter == '*']
        for occ in occs:
            # Check to make sure there are exactly two numbers
            all_nums = {} # key: coords of the start. value: num
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    # print(f'finding nums of line {grid[col+i]} at index {occ+j} in row num {col+i}')
                    ret = find_nums(grid[col+i], occ+j, col+i) #str and index
                    # print(f'returned {ret[0]} and {ret[1]}')
                    if ret[0] == (-1,-1) or ret[0] in all_nums:
                        continue
                    all_nums[ret[0]] = ret[1]
            # Found all numbers, check length of ret
            print(f'for index {col, occ}, all nums is ')
            print(all_nums)