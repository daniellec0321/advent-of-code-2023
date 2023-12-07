import sys

def puzzle1():
    # Filter through mappings
    lines = list(filter(lambda l: l != '\n', sys.stdin.readlines()))
    seeds = list(map(int, list(filter(lambda l: l != '', \
            lines[0].rstrip().split(':')[1].rstrip().split(' ')))))
    it = 1
    for line in lines[1:]:
        if '-' in line:
            continue
        dst_start = int(line.split(' '[0]))
        src_start = int(line.split(' '[1]))
        range = int(line.split(' '[2]))
        dst = list(range(dst_start, dst_start+range+1))
        src = list(range(src_start, src_start+range+1))
    



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