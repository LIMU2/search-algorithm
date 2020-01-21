# for r in range(row):
#     for c in range(column):
#         if maze[r][c] == '%':
#             maze[r][c] = 1
#         elif maze[r][c] == ' ':
#             maze[r][c] = 0
#         elif maze[r][c] == '.':  # the endpoint also needs to be transformed to zero
#             maze[r][c] = 0

# while len(stack) > 0:
#     current_point = stack.pop()
#     if maze[current_point[0]][current_point[1]] == 'P':
#         maze[current_point[0]][current_point[1]] = 0
#         parent[current_point[0]][current_point[1]] = [start_point[0], start_point[1]]
#     for d in direction:
#         next_point = d(current_point)
#         if maze[next_point[0]][next_point[1]] != 1 and (
#                 maze[next_point[0]][next_point[1]] > maze[current_point[0]][current_point[1]] + 1 or
#                 maze[next_point[0]][next_point[1]] == 0
#         ):
#             stack.append(next_point)
#             maze[next_point[0]][next_point[1]] = maze[current_point[0]][current_point[1]] + 1
#             parent[next_point[0]][next_point[1]] = [current_point[0], current_point[1]]
# if maze[endpoint[0]][endpoint[1]] == 0:  # can not reach the endpoint
#     print("Sorry, this maze has no result!")
#     return False
