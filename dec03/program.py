import re

if __name__ == '__main__':
    
    # Puzzle 1
    f = open('test.txt', 'r')

    # Making the puzzle grid (also making a buffer)
    grid = [x.strip() for x in f.readlines()]
    grid = [''.join('.' for _ in grid[0])] + grid + [''.join('.' for _ in grid[0])]
    grid = ['.' + line + '.' for line in grid]
    sum = 0

    # Check each line in the puzzle grid
    for line in grid:
        nums = [x for x in line.split('.') if x.isdigit()]
        if not nums:
            continue
        # Loop through numbers
        for num in nums:
            indices = [m.start() for m in re.finditer(num, line)]
            # Loop through all occurences of numbers
            for index in indices:
                # Get all tuples
                tuples = []
                for i in range(-1, len(num)+1):
                    tuples += [(index+i,index-1), (index+i,index), (index+i,index+1)]
                # Check every tuple to see if there is a symbol
                no_symbol = True
                for t in tuples:
                    if (not grid[t[0]][t[1]].isdigit()) and (grid[t[0]][t[1]] != '.'):
                        print(f'with num {num}, index {t} is a symbol')
                        print(grid[t[0]][t[1]])
                        no_symbol = False
                        break
                
                if no_symbol:
                    continue

                print(f'adding on number {num}')
                sum += int(num)

    f.close()
    print(f'The answer to question 1 is {sum}')