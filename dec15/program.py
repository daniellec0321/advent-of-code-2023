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

    def hash(self, string: str) -> int:
        current_value = 0
        for char in string:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256
        return current_value

    def solve_puzzle(self, stream=sys.stdin):

        boxes = dict() # Key: integer representing the box number. # Value: a list of tuples
        for elem in sys.stdin.readline().strip().split(','):
            label = ''
            op = '='
            focal_length = -1
            if '-' in elem:
                label = elem.split('-')[0]
                op = '-'
            else:
                label = elem.split('=')[0]
                focal_length = int(elem.split('=')[1])
            box_number = self.hash(label)
            if op == '-':
                # check for box number
                if box_number in boxes:
                    found = -1
                    for idx, t in enumerate(boxes[box_number]):
                        if label == t[0]:
                            found = idx
                            break
                    if found != -1:
                        del boxes[box_number][found]
                    # Check for empty dictionary
                    if len(boxes[box_number]) == 0:
                        del boxes[box_number]
            # need to do the = thing
            else:
                if not box_number in boxes:
                    boxes[box_number] = [(label, focal_length)]
                else:
                    # see if box already exists
                    found = False
                    for idx, t in enumerate(boxes[box_number]):
                        if t[0] == label:
                            found = True
                            boxes[box_number][idx] = (label, focal_length)
                            break
                    if not found:
                        boxes[box_number].append((label, focal_length))
        
        # Add up all of the values in boxes
        sum = 0
        for key, value in boxes.items():
            for idx, t in enumerate(value):
                sum += (key+1)*(idx+1)*(t[1])
        print(f'The answer to puzzle 2 is {sum}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()