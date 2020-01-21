# greedy best-first search
# the evaluation function is f(n)=h(n), heuristic function, denoted by h(n), which estimates
# the distance to the goal node.
# 1. If the successor's heuristic is better than its parent, the successor is set at the
# front of the queue (with the parent reinserted directly behind it), and the loop restarts.
# 2. Else, the successor is inserted into the queue (in a location determined by its heuristic value).
# 3. The procedure will evaluate the remaining successors (if any) of the parent.
import DepthFirstSearch
from queue import PriorityQueue


def manhattan_distance(point1, point2):
    distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return distance


def greedy_best_first_search(file_path):
    [row, column, maze] = DepthFirstSearch.read_maze(file_path)
    start_point = DepthFirstSearch.find_start_point(maze)
    endpoint = DepthFirstSearch.find_endpoint(maze)
    queue = PriorityQueue()
    queue.put(start_point, 0)
    direction = [
        lambda point: (point[0] - 1, point[1]),  # up
        lambda point: (point[0] + 1, point[1]),  # down
        lambda point: (point[0], point[1] - 1),  # left
        lambda point: (point[0], point[1] + 1),  # right
    ]
    came_from = {}
    came_from[start_point[0], start_point[1]] = None
    while queue.qsize() > 0:
        current_point = queue.get()
        if current_point == endpoint:
            print("find the result!")
            return True
        # current_distance = manhattan_distance(current_point, endpoint)
        # maze[current_point[0]][current_point[1]] = current_distance
        for d in direction:
            successor = d(current_point)
            if successor not in came_from:
                successor_distance = manhattan_distance(successor, endpoint)
                queue.put(successor, successor_distance)
                came_from[successor] = current_point
            # if maze[successor[0]][successor[1]] == ' ':
            #     successor_distance = manhattan_distance(successor, endpoint)
            #     maze[successor[0]][successor[1]] = successor_distance
            #     if current_distance > successor_distance:
            #         stack.append(successor)
            #
            #     for s in stack:
            #         if maze[s[0]][s[1]] <= successor_distance:
            #             stack.insert(stack.index(s), successor)
            #             break

        # for d in direction:
        #     successor = d(current_point)
        #     if maze[successor[0]][successor[1]] == ' ':
        #         successor_distance = manhattan_distance(successor, endpoint)
        #     if successor_distance < current_distance:
        #         stack.append(successor)
        #         maze[successor[0]][successor[1]] = successor_distance
        #         break
        #     else:
        #         for s in stack:
        #             if maze[s[0]][s[1]] <= successor_distance:
        #                 stack.insert(stack.index(s), successor)
        #                 break
    # else:
    #     a = stack.pop()
    #     maze[a[0]][a[1]] = -1

    if maze[endpoint[0]][endpoint[1]] == '.':
        print("No result!")
        return False


if __name__ == '__main__':
    # path = './MediumMaze.txt'
    # path = './BigMaze.txt'
    path = './OpenMaze.txt'
    # print_shortest_route(path)
    greedy_best_first_search(path)
    # print(manhattan_distance([17, 13], DepthFirstSearch.find_endpoint(path)))
    # print(manhattan_distance([18, 14], DepthFirstSearch.find_endpoint(path)))
    # print(manhattan_distance([17, 14], DepthFirstSearch.find_endpoint(path)))
