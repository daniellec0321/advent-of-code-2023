import sys

def puzzle1():
    # Filter through mappings
    lines = [x.rstrip() for x in list(filter(lambda l: l != '\n', sys.stdin.readlines()))]
    seeds = list(map(int, list(filter(lambda l: l != '', \
            lines[0].rstrip().split(':')[1].rstrip().split(' ')))))
    it = 1
    for line in lines[1:]:
        # print(f'line is {line}')
        if '-' in line:
            continue
        dst_start = int(line.split(' ')[0])
        src_start = int(line.split(' ')[1])
        range_amount = int(line.split(' ')[2])
        dst = list(range(dst_start, dst_start+range_amount))
        src = list(range(src_start, src_start+range_amount))
        # print(f'dst is from {dst[0]} to {dst[-1]}')
        # print(f'src is from {src[0]} to {src[-1]}')
        # Update each seed if needed
        for seed_idx, seed in enumerate(seeds):
            try:
                old_seed = seeds[seed_idx]
                src_index = src.index(seed)
                seeds[seed_idx] = dst[src_index]
                if seed_idx == 1 and ('18 25 70' in line):
                    print(line)
                    print(f'src range is {src[0]} to {src[-1]}')
                    print(f'dst range is {dst[0]} to {dst[-1]}')
                    print(f'Updated seed {old_seed} to {dst[src_index]}')
            except ValueError:
                pass
            # if src_index != -1:
            #     seeds[seed_idx] = dst[src_index]
            #     print(f'Updated seed {seed} to {seeds[seed_idx]}')

    print(f'Seeds are {seeds}')
    


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