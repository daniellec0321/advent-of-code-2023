import sys

def puzzle1():
    lines = [x.rstrip() for x in list(filter(lambda l: l != '\n', sys.stdin.readlines()))]
    seeds = list(map(int, list(filter(lambda l: l != '', \
            lines[0].rstrip().split(':')[1].rstrip().split(' ')))))
    updated = [False] * len(seeds)
    for line in lines[1:]:
        if '-' in line:
            updated = [False] * len(seeds)
            continue
        dst_start = int(line.split(' ')[0])
        src_start = int(line.split(' ')[1])
        range_amount = int(line.split(' ')[2])
        src_end = src_start + range_amount
        for seed_idx, seed in enumerate(seeds):
           if (src_start <= seed <= src_end) and (not updated[seed_idx]):
               update_val = seed - src_start
               seeds[seed_idx] = dst_start + update_val
               updated[seed_idx] = True

    print(f'The answer to puzzle 1 is {min(seeds)}')
    


def puzzle2():
    pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()