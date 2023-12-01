import sys

VALUES = {'1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', \
            '7': '7', '8': '8', '9': '9', '0': '0', 'one': '1', 'two': '2', \
            'three': '3', 'four': '4', 'five': '5', 'six': '6', \
            'seven': '7', 'eight': '8', 'nine': '9'}

if __name__ == '__main__':
    
    # Puzzle 1
    f = open('input.txt', 'r')
    sum = 0
    for line in list(map(lambda l: l.rstrip(), f.readlines())):
        num = ''
        for letter in line:
            if letter.isdigit():
                num += letter
                break
        for letter in reversed(line):
            if letter.isdigit():
                num += letter
                break
        sum += int(num)

    f.close()
    print(f'The first puzzle answer is {sum}')

    # Puzzle 2
    f = open('input.txt', 'r')
    sum = 0
    for line in list(map(lambda l: l.rstrip(), f.readlines())):
        first_digit = ''
        first_digit_index = sys.maxsize
        last_digit = ''
        last_digit_index = -1
        for value in VALUES:
            curr_index = line.find(value)
            if (curr_index >= 0) and (curr_index < first_digit_index):
                first_digit_index = curr_index
                first_digit = VALUES[value]
            curr_index = line.rfind(value)
            if curr_index > last_digit_index:
                last_digit_index = curr_index
                last_digit = VALUES[value]
        sum += int(first_digit + last_digit)
    
    f.close()
    print(f'The second puzzle answer is {sum}')