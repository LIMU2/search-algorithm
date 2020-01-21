# DFS
# 除了需要记录该节点位置，也要记录该节点是否被访问过（flag）
# 创建一个空栈，首先将入口位置进栈。当栈不空时循环：获取栈顶元素，寻找下一个可走的相邻方块，如果找不到可走的相邻方块，说明当前位置是死胡同，进行回溯（就是讲当前位置出栈，看前面的点是否还有别的出路）
# 1. 起始位置坐标(x0, y0)
# 2. 向相邻的方向移动，创建新路径
# 3. 如果不是墙，则重复第二步；如果是墙，则路径截至；如果是豆子，则记录此路径
# 4. 如果5条路径都没有，则返回上一个（栈）
# 5. 比较所有可行路径
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


def depth_first_search(file_path):
    # transform the file into list
    [row, column, maze] = read_maze(file_path)
    start_point = find_start_point(maze)
    endpoint = find_endpoint(maze)
    copy_maze = copy.deepcopy(maze)
    print("start point: ", start_point)
    print("endpoint: ", endpoint)
    # push start point into stack
    stack = [start_point]
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
    while len(stack) > 0:
        current_point = stack.pop()
        for d in direction:
            next_point = d(current_point)
            if maze[next_point[0]][next_point[1]] != '%' and (
                    dist[next_point[0]][next_point[1]] > dist[current_point[0]][current_point[1]] + 1 or
                    dist[next_point[0]][next_point[1]] == -1):
                dist[next_point[0]][next_point[1]] = dist[current_point[0]][current_point[1]] + 1
                parent[next_point[0]][next_point[1]] = [current_point[0], current_point[1]]
                stack.append(next_point)
                count += 1
    if dist[endpoint[0]][endpoint[1]] == -1:  # can not reach the endpoint
        print("Sorry, this maze has no result!")
        return False
    else:
        print("I expanded %d nodes" % count)
        return row, column, start_point, endpoint, parent, copy_maze


def print_shortest_route(path):
    [row, column, start_point, endpoint, parent, maze] = depth_first_search(file_path=path)
    x = endpoint[0]
    y = endpoint[1]
    maze[x][y] = '🚩'
    x, y = parent[x][y]
    step = 2  # including start point and endpoint
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
