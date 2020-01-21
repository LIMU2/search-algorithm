# greedy best-first search
# the evaluation function is f(n)=h(n), heuristic function, denoted by h(n), which estimates
# the distance to the goal node.
# 1. If the successor's heuristic is better than its parent, the successor is set at the
# front of the queue (with the parent reinserted directly behind it), and the loop restarts.
# 2. Else, the successor is inserted into the queue (in a location determined by its heuristic value).
# 3. The procedure will evaluate the remaining successors (if any) of the parent.
import DepthFirstSearch
from queue import PriorityQueue
import copy


def manhattan_distance(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance


def greedy_best_first_search(file_path):
    [row, column, maze] = DepthFirstSearch.read_maze(file_path)
    start_point = DepthFirstSearch.find_start_point(maze)
    start_point = (start_point[0], start_point[1])
    endpoint = DepthFirstSearch.find_endpoint(maze)
    print("start point: ", start_point)
    print("endpoint: ", endpoint)
    direction = [
        lambda point: (point[0] - 1, point[1]),  # up
        lambda point: (point[0] + 1, point[1]),  # down
        lambda point: (point[0], point[1] - 1),  # left
        lambda point: (point[0], point[1] + 1),  # right
    ]
    queue = PriorityQueue()
    queue.put((0, start_point))
    came_from = {}
    came_from[start_point[0], start_point[1]] = None
    count = 0
    while not queue.empty():
        current_point = queue.get()
        if current_point[1][0] == endpoint[0] and current_point[1][1] == endpoint[1]:
            x = endpoint[0]
            y = endpoint[1]
            maze[x][y] = '🚩'
            x, y = came_from[x, y]
            copy_maze = copy.deepcopy(maze)
            step = 2
            while x != start_point[0] or y != start_point[1]:
                copy_maze[x][y] = '0'
                x, y = came_from[x, y]
                step += 1
            for r in range(row):
                for c in range(column):
                    print("%2s" % (copy_maze[r][c]), end=' ')  # default: end='\n'
                print()
            print("I expanded %d nodes" % count)
            print("steps: ", step)
            print("find the result!")
            return True
        for d in direction:
            successor = d(current_point[1])
            if successor not in came_from and maze[successor[0]][successor[1]] != '%':
                successor_distance = manhattan_distance(successor, endpoint)
                queue.put((successor_distance, successor))
                came_from[successor] = current_point[1]
                count += 1
    # can not reach the endpoint
    print("Sorry, this maze has no result!")
    return False


if __name__ == '__main__':
    path = './MediumMaze.txt'
    # path = './BigMaze.txt'
    # path = './OpenMaze.txt'
    # print_shortest_route(path)
    greedy_best_first_search(path)
