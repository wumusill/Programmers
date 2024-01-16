def solution(dirs):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    route = []
    x, y = 0, 0
    for dir in dirs:
        if dir == 'U':
            nx = x + dx[0]
            ny = y + dy[0]
        elif dir == 'D':
            nx = x + dx[1]
            ny = y + dy[1]
        elif dir == 'L':
            nx = x + dx[2]
            ny = y + dy[2]
        elif dir == 'R':
            nx = x + dx[3]
            ny = y + dy[3]

        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue

        if [x, y, nx, ny] not in route and [nx, ny, x, y] not in route:
            route.append([x, y, nx, ny])
            route.append([nx, ny, x, y])

        x, y = nx, ny

    answer = len(route) // 2

    return answer
#########################################################################################################
def solution(dirs):
    x, y = 0, 0
    d = {'U':(0, 1), 'D':(0, -1), 'L':(-1, 0), 'R':(1, 0)}
    route = set()
    for cmd in dirs:
        nx, ny = x + d[cmd][0], y + d[cmd][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            route.add((x, y, nx, ny))
            route.add((nx, ny, x, y))
            x, y = nx, ny
    return len(route) // 2