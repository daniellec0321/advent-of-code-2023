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
    seeds = list()
    for i in range(0, len(seed_vals), 2):
        seeds.append((seed_vals[i], seed_vals[i+1]))
    range_changes = list()
    for line in lines[1:]:
        # print(f'at line {line}')
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
                    elif src_start < seed_start+seed_range: # seed ends within the range and start outside the range
                        # default options
                        unaffected = (seed_start, (src_start-seed_start))
                        seeds_copy.append(unaffected)
                        affected_range = (src_start, seed_range-(src_start-seed_start))
                        # edge case: encoding is completely wrapped in seed
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

    #         while seeds:
    #             seed_start, seed_range = seeds.pop()
    #             # go through rangechanges
    #             no_change = True
    #             for dst_start, src_start, code_range in range_changes:
    #                 if (src_start <= seed_start < src_start+code_range): # seed starts after source OR is completely within range
    #                     affected_range = (seed_start, seed_range)
    #                     if (seed_start + seed_range) > (src_start + code_range):
    #                         # write unaffected
    #                         unaffected = (src_start+code_range, (seed_start+seed_range) - (src_start+code_range))
    #                         seeds.append(unaffected)
    #                         # write affected
    #                         affected_range = (seed_start, (src_start+code_range)-seed_start)
    #                     # translate affected
    #                     affected = (affected_range[0]+(dst_start-src_start), affected_range[1])
    #                     new_seeds.append(affected)
    #                     no_change = False 
    #                     break
    #                 elif src_start < seed_start+seed_range: # seed ends within the range and start outside the range
    #                     # default options
    #                     unaffected = (seed_start, (src_start-seed_start))
    #                     seeds.append(unaffected)
    #                     no_change = False
    #                     break
    #             if no_change:
    #                 new_seeds.append((seed_start, seed_range))

    #         seeds = new_seeds.copy()
    #         range_changes = list()
    #     else:
    #         # add on the range change
    #         range_changes.append(tuple(list(map(int, line.split(' ')))))
    
    # # Compute last set of range changes
    # if len(range_changes) != 0:
    #     new_seeds = set()
    #     print('Range changes is:')
    #     print(range_changes)
    #     seeds = new_seeds.copy()
    #     range_changes = set()

        # dst_start = int(line.split(' ')[0])
        # src_start = int(line.split(' ')[1])
        # range_amount = int(line.split(' ')[2])
        # src_end = src_start + range_amount
        # copy = list(seeds)
        # while copy:
        #     # seeds.remove(seed)
        #     # new_seeds.add(seed)
        #     seed_start = seed[0]
        #     seed_end = seed[0] + seed[1]
        #     if (src_start <= seed_start < src_end):
        #         print(f'for line {line} and seed {seed}, need to update')
        #         seeds.remove(seed)
        #         # Split range into two tuples
        #         # If the entire seed is affected
        #         affected = (seed_start, seed_end)
        #         if seed_end > src_end:
        #             affected = (69, 69)
        #             # unaffected equals something that we need to put into seeds
        #     elif (src_start < seed_end <= src_end):
        #         pass

    print(f'The seeds are {seeds}')
    print(f'The answer to puzzle 2 is {min(seeds)}')



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        puzzle1()
    elif sys.argv[1] == '2':
        puzzle2()