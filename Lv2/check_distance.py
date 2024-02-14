from collections import deque


def check(row, col, place):
    q = deque([(row, col, 0)])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[True for _ in range(5)] for _ in range(5)]
    visited[row][col] = False
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:          # 대기실 범위 밖이면 continue
                continue
            if place[nx][ny] == "X":                            # 파티션이면 continue
                continue
            new_d = d + 1
            if place[nx][ny] == 'O' and visited[nx][ny]:        # 책상이면 방문 처리 후 좌표와 거리 큐에 삽입
                visited[nx][ny] = False
                q.append((nx, ny, d + 1))

            if place[nx][ny] == 'P' and visited[nx][ny]:        # 사람이면 거리 확인
                if new_d > 2:                                   # 3 이상은 괜찮고, 2 이하면 안됨
                    return True
                else:
                    return False

    return True


def solution(places):
    answer = []
    for place in places:
        result = True
        for row in range(5):
            for col in range(5):
                if place[row][col] == 'P':                      # P 마다 거리두기 확인
                    result = result and check(row, col, place)  # 하나라도 불가능한 경우가 있으면 False

        answer.append(1 if result else 0)                       # 거리두기 지킨 경우라면 1 기록

    return answer