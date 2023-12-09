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
    lines = [x.rstrip() for x in list(filter(lambda l: l != '\n', sys.stdin.readlines()))]
    seed_vals = list(map(int, list(filter(lambda l: l != '', \
            lines[0].rstrip().split(':')[1].rstrip().split(' ')))))
    seeds = set()
    updated = dict()
    for i in range(0, len(seed_vals), 2):
        seeds.add((seed_vals[i], seed_vals[i+1]))
    new_seeds = set()
    for line in lines[1:]:
        # print(f'at line {line}')
        if '-' in line:
            seeds.update(new_seeds)
            new_seeds = set()
            continue
        dst_start = int(line.split(' ')[0])
        src_start = int(line.split(' ')[1])
        range_amount = int(line.split(' ')[2])
        src_end = src_start + range_amount
        copy = seeds.copy()
        # for seed in seeds:
        #     if 1:
        #     # if (src_start <= seed <= src_end) and (not updated[(seed)]):
        #         pass
        #     else:
        #        new_seeds.add(seed)
        for seed in copy:
            # seeds.remove(seed)
            # new_seeds.add(seed)
            seed_start = seed[0]
            seed_end = seed[0] + seed[1]
            if (src_start <= seed_start < src_end):
                print(f'for line {line} and seed {seed}, need to update')
                seeds.remove(seed)
                # Split range into two tuples
                # If the entire seed is affected
                affected = (seed_start, seed_end)
                if seed_end > src_end:
                    affected = (69, 69)
                    # unaffected equals something that we need to put into seeds
            elif (src_start < seed_end <= src_end):
                pass

    # print(f'The answer to puzzle 2 is {min(seeds)}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()