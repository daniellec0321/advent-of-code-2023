import sys
import heapq as hq

class Puzzle1():

    def addt(self, t1, t2):
        return tuple([sum(x) for x in zip(t1, t2)])

    def solve_puzzle(self, stream=sys.stdin):
        grid = [list(map(int, list(x.strip()))) for x in stream.readlines()]
        frontier = list() # Tuple. (total heat loss, times going straight, direction, (path))
        visited = set()
        # neighbors = {'right': [(-1,0,'up'),(1,0,'down'),(0,1,'right')], \
        #              'left': [(-1,0,'up'),(1,0,'down'),(0,-1,'left')], \
        #              'down': [(1,0,'down'),(0,1,''),(0,-1)], \
        #              'up': [(-1,0),(0,1),(0,-1)]}
        neighbors = {'right': [((1,0),'up'),((1,0),'down'),((0,1),'right')], \
                     'left': [((-1,0),'up'),((1,0),'down'),((0,-1),'left')], \
                     'down': [((1,0),'down'),((0,1),'right'),((0,-1),'left')], \
                     'up': [((-1,0),'up'),((0,1),'right'),((0,-1),'left')]}
        
        goal = (len(grid)-1, len(grid[0])-1)

        # initialize queue
        hq.heappush(frontier, (0, 0, 'right', [(0,0)], {(0,0)}))
        hq.heappush(frontier, (0, 0, 'down', [(0,0)], {(0,0)}))

        loops = 0

        while frontier:
            loops += 1
            if loops % 1000 == 0:
                print(f'On loop {loops}')
                print(heat_loss)
            heat_loss, times_straight, direction, path, visited = hq.heappop(frontier)
            # print(heat_loss)
            curr = path[-1]
            # print(curr)
            # Check if at the end
            if curr == goal:
                print(path)
                break
            # Loop through neighbors
            for to_add, new_dir in neighbors[direction]:
                new_loc = self.addt(to_add, path[-1])
                # Check if in bounds
                if not (0 <= new_loc[0] < len(grid)) or not (0 <= new_loc[1] < len(grid[0])):
                    continue
                # Check times going straight
                if direction == new_dir and times_straight == 2:
                    continue
                # Check if this has already been visited
                if new_loc in visited:
                    continue
                # Add onto frontier
                heat_loss += grid[new_loc[0]][new_loc[1]]
                if direction == new_dir:
                    times_straight += 1
                else:
                    times_straight = 0
                new_path = path.copy()
                new_path.append(new_loc)
                new_visited = visited.copy()
                new_visited.add(new_loc)
                hq.heappush(frontier, (heat_loss, times_straight, new_dir, new_path, new_visited))



class Puzzle2():
    def solve_puzzle(self, stream=sys.stdin):
        pass



if __name__ == '__main__':
    
    if len(sys.argv) != 2 or (sys.argv[1] != '1' and sys.argv[1] != '2'):
        print('Please include \'1\' or \'2\' to indicate which puzzle to test.')
        sys.exit(1)

    if sys.argv[1] == '1':
        SOL = Puzzle1()
    elif sys.argv[1] == '2':
        SOL = Puzzle2()

    SOL.solve_puzzle()