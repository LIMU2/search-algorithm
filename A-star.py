# A-star Algorithm
# uses both the actual distance from the start and the estimated distance to the goal.
import DepthFirstSearch
from queue import PriorityQueue
import copy


def manhattan_distance(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance


def a_star_algorithm(file_path):
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
    cost_so_far = {}
    came_from[start_point[0], start_point[1]] = None
    cost_so_far[start_point[0], start_point[1]] = 0
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
            new_cost = cost_so_far[current_point[1]] + 1
            if (successor not in cost_so_far or new_cost < cost_so_far[successor]) and maze[successor[0]][
                successor[1]] != '%':
                cost_so_far[successor] = new_cost
                successor_distance = new_cost + manhattan_distance(successor, endpoint)
                queue.put((successor_distance, successor))
                came_from[successor] = current_point[1]
                count += 1
    # can not reach the endpoint
    print("Sorry, this maze has no result!")
    return False


if __name__ == '__main__':
    # path = './MediumMaze.txt'
    # path = './BigMaze.txt'
    # path = './OpenMaze.txt'
    path = './bigDots.txt'
    # print_shortest_route(path)
    a_star_algorithm(path)
