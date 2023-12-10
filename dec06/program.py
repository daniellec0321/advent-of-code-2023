import sys

def puzzle1():
    times = list(map(int, filter(lambda l: l != '', \
            sys.stdin.readline().rstrip().split(':')[1].rstrip().split(' '))))
    distances = list(map(int, filter(lambda l: l != '', \
            sys.stdin.readline().rstrip().split(':')[1].rstrip().split(' '))))
    product = 1
    for time, best_distance in zip(times, distances):
        ways_to_win = 0
        for button_hold in range(1, time):
            time_left = time-button_hold
            distance_traveled = time_left*button_hold
            if (distance_traveled > best_distance):
                ways_to_win += 1
        product *= ways_to_win
    print(f'The answer to puzzle 1 is {product}')



def puzzle2():
    time = int(''.join(list(filter(lambda l: l != '', \
            sys.stdin.readline().rstrip().split(':')[1].rstrip().split(' ')))))
    best_distance = int(''.join(list(filter(lambda l: l != '', \
            sys.stdin.readline().rstrip().split(':')[1].rstrip().split(' ')))))
    ways_to_win = 0
    for button_hold in range(1, time):
        time_left = time-button_hold
        distance_traveled = time_left*button_hold
        if (distance_traveled > best_distance):
            ways_to_win += 1
    print(f'The answer to puzzle 2 is {ways_to_win}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()