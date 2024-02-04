# 땅의 길이만큼 리스트 생성 (result)
# 시추관을 꽂았을 때 처음 만나는 석유의 양 계산
# 석유의 너비 좌표를 순회하여 result[좌표]에 석유의 양 기록
from collections import deque


def solution(land):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = [0 for _ in range(len(land[0]))]
    visited = [[True for _ in range(len(land[0]))] for _ in range(len(land))]
    for a in range(len(land)):
        for b in range(len(land[0])):
            if land[a][b] == 1 and visited[a][b]:
                q = deque([(a, b)])
                visited[a][b] = False
                min_y, max_y = b, b
                res = 0

                while q:
                    x, y = q.popleft()
                    max_y = max(y, max_y)
                    min_y = min(y, min_y)
                    res += 1
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or ny < 0 or nx >= len(land) or ny >= len(land[0]):
                            continue
                        if visited[nx][ny] and land[nx][ny] == 1:
                            visited[nx][ny] = False
                            q.append((nx, ny))

                for y in range(min_y, max_y + 1):
                    result[y] += res

        answer = max(result)

    return answer