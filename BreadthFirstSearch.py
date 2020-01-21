# BFS

import copy


def find_start_point(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][j] == 'P':
                return [i, j]


def find_endpoint(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            if my_list[i][j] == '.':
                return [i, j]


def read_maze(file_path):
    file = open(file_path, 'r')
    content = file.read()
    maze = []
    column = content.find('\n') + 1
    for i in range(0, len(content), column):
        maze.append(list(content)[i:i + column])
    row = len(maze)
    column = column - 1
    return row, column, maze


def breadth_first_search(file_path):
    # transform the file into list
    [row, column, maze] = read_maze(file_path)
    start_point = find_start_point(maze)
    endpoint = find_endpoint(maze)
    copy_maze = copy.deepcopy(maze)
    print("start point: ", start_point)
    print("endpoint: ", endpoint)
    # push start point into queue
    queue = [start_point]
    # initialize
    direction = [
        lambda point: (point[0] - 1, point[1]),  # up
        lambda point: (point[0] + 1, point[1]),  # down
        lambda point: (point[0], point[1] - 1),  # left
        lambda point: (point[0], point[1] + 1),  # right
    ]
    dist = [[-1 for r in range(column)] for c in range(row)]
    parent = [[start_point for r in range(column)] for c in range(row)]
    # search
    count = 0
    while len(queue) > 0:
        current_point = queue.pop(0)
        for d in direction:
            next_point = d(current_point)
            if maze[next_point[0]][next_point[1]] != '%' and (
                    dist[next_point[0]][next_point[1]] > dist[current_point[0]][current_point[1]] + 1 or
                    dist[next_point[0]][next_point[1]] == -1):
                dist[next_point[0]][next_point[1]] = dist[current_point[0]][current_point[1]] + 1
                parent[next_point[0]][next_point[1]] = [current_point[0], current_point[1]]
                queue.append(next_point)
                count += 1
            elif maze[next_point[0]][next_point[1]] == '.':
                dist[next_point[0]][next_point[1]] = dist[current_point[0]][current_point[1]] + 1
                parent[next_point[0]][next_point[1]] = [current_point[0], current_point[1]]
                queue.append(next_point)
                count += 1
                return row, column, start_point, endpoint, parent, copy_maze
    if dist[endpoint[0]][endpoint[1]] == -1:  # can not reach the endpoint
        print("Sorry, this maze has no result!")
        return False
    else:
        print("I expanded %d nodes" % count)
        return row, column, start_point, endpoint, parent, copy_maze


def print_shortest_route(path):
    [row, column, start_point, endpoint, parent, maze] = breadth_first_search(file_path=path)
    x = endpoint[0]
    y = endpoint[1]
    maze[x][y] = '🚩'
    x, y = parent[x][y]
    step = 2
    while x != start_point[0] or y != start_point[1]:
        maze[x][y] = '0'
        x, y = parent[x][y]
        step += 1
    for r in range(row):
        for c in range(column):
            print("%2s" % (maze[r][c]), end=' ')  # default: end='\n'
        print()
    print("steps: ", step)


if __name__ == '__main__':
    path = './MediumMaze.txt'
    # path = './BigMaze.txt'
    # path = './OpenMaze.txt'
    print_shortest_route(path)
