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
    '''temporary'''
    # f = open('test.txt', 'r')
    # temp = f.readlines()
    # f.close()
    '''end of temp'''
    lines = [x.rstrip() for x in list(filter(lambda l: l != '\n', sys.stdin.readlines()))]
    # lines = [x.rstrip() for x in list(filter(lambda l: l != '\n', temp))]
    seed_vals = list(map(int, list(filter(lambda l: l != '', \
            lines[0].rstrip().split(':')[1].rstrip().split(' ')))))
    seeds = list()
    for i in range(0, len(seed_vals), 2):
        seeds.append((seed_vals[i], seed_vals[i+1]))
    range_changes = list()
    for line in lines[1:]:
        if '-' in line:
            if len(range_changes) == 0:
                continue
            new_seeds = list()
            for dst_start, src_start, code_range in range_changes:
                seeds_copy = list()
                for seed_start, seed_range in seeds:
                    # if unaffected, push to copy
                    # if affected, push to newseeds
                    if (src_start <= seed_start < src_start+code_range): # seed starts after source OR is completely within range
                        affected_range = (seed_start, seed_range)
                        if (seed_start + seed_range) > (src_start + code_range):
                            # write unaffected
                            unaffected = (src_start+code_range, (seed_start+seed_range) - (src_start+code_range))
                            seeds_copy.append(unaffected)
                            # write affected
                            affected_range = (seed_start, (src_start+code_range)-seed_start)
                        # translate affected
                        affected = (affected_range[0]+(dst_start-src_start), affected_range[1])
                        new_seeds.append(affected)
                    elif (src_start < seed_start+seed_range) and (src_start+code_range > seed_start): # seed ends within the range and start outside the range
                        # default options
                        unaffected = (seed_start, (src_start-seed_start))
                        seeds_copy.append(unaffected)
                        affected_range = (src_start, seed_range-(src_start-seed_start))
                        if (src_start+code_range) < (seed_start+seed_range):
                            unaffected = (src_start+code_range, (seed_start+seed_range)-(src_start+code_range))
                            seeds_copy.append(unaffected)
                            affected_range = (src_start, affected_range[1]-unaffected[1])
                        # translate affected
                        affected = (affected_range[0]+(dst_start-src_start), affected_range[1])
                        new_seeds.append(affected)
                    else:
                        seeds_copy.append((seed_start, seed_range))
                seeds = seeds_copy.copy()
            seeds += new_seeds
            range_changes = list()
        
        else:
            # add on the range change
            range_changes.append(tuple(list(map(int, line.split(' ')))))

    # Translate last set of range changes
    for dst_start, src_start, code_range in range_changes:
        seeds_copy = list()
        for seed_start, seed_range in seeds:
            # if unaffected, push to copy
            # if affected, push to newseeds
            if (src_start <= seed_start < src_start+code_range): # seed starts after source OR is completely within range
                affected_range = (seed_start, seed_range)
                if (seed_start + seed_range) > (src_start + code_range):
                    # write unaffected
                    unaffected = (src_start+code_range, (seed_start+seed_range) - (src_start+code_range))
                    seeds_copy.append(unaffected)
                    # write affected
                    affected_range = (seed_start, (src_start+code_range)-seed_start)
                # translate affected
                affected = (affected_range[0]+(dst_start-src_start), affected_range[1])
                new_seeds.append(affected)
            elif (src_start < seed_start+seed_range) and (src_start+code_range > seed_start): # seed ends within the range and start outside the range
                # default options
                unaffected = (seed_start, (src_start-seed_start))
                seeds_copy.append(unaffected)
                affected_range = (src_start, seed_range-(src_start-seed_start))
                if (src_start+code_range) < (seed_start+seed_range):
                    unaffected = (src_start+code_range, (seed_start+seed_range)-(src_start+code_range))
                    seeds_copy.append(unaffected)
                    affected_range = (src_start, affected_range[1]-unaffected[1])
                # translate affected
                affected = (affected_range[0]+(dst_start-src_start), affected_range[1])
                new_seeds.append(affected)
            else:
                seeds_copy.append((seed_start, seed_range))
        seeds = seeds_copy.copy()
    seeds += new_seeds
    range_changes = list()
         
    ans = sys.maxsize
    for seed, r in seeds:
        ans = min(ans, seed)
    print(f'The answer to puzzle 2 is {ans}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()