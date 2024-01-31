# 시간 초과
from collections import deque


def solution(n, m, x, y, r, c, k):
    direction = {'u':[-1, 0], 'd':[1, 0], 'l':[0, -1], 'r':[0, 1]}  # 상하좌우

    q = deque([(x, y, '')])
    while q:
        x, y, command = q.popleft()

        if x == r and y == c and len(command) == k:                 # k 번째로 목적지 도착했으면 후보군에 좌표 추가
            answer.append(command)

        for key in direction:                                       # 상하좌우 순회
            nx = x + direction[key][0]
            ny = y + direction[key][1]
            new = command + key
            if 0 < nx <= n and 0 < ny <= m and len(new) <= k:       # map 벗어나지 않고 명령어가 k보다 짧거나 같으면 q에 삽입
                q.append((nx, ny, new))

    if answer:                                                      # bfs 후 결과물 있으면 오름차순 정렬 후 첫 명령어 반환
        answer.sort()
        return answer[0]
    else:                                                           # 결과물 없으면 impossible 반환
        return 'impossible'
#######################################################################################################################
from collections import deque


def solution(n, m, x, y, r, c, k):
    direction = {'d':[1, 0], 'l':[0, -1], 'r':[0, 1], 'u':[-1, 0]}  # 명령어 사전순 탐색

    shortest = abs(x - r) + abs(y - c)                              # 최단 거리가 k보다 작으면 목적지 도착 불가능
    if k < shortest or (k - shortest) % 2:                          # (k - 최단 거리)가 홀수면 목적지 도착 불가능
        return 'impossible'                                         # 짝수이어야만 목적지 도착 후 다른 곳 찍고 k 번째에 도착 가능

    q = deque([(x, y, '')])
    while q:
        x, y, command = q.popleft()
        if x == r and y == c and len(command) == k:                 # k 번의 이동으로 목적지 도착했으면 명령어 반환
            return command

        if x == r and y == c and (k - len(command)) % 2:            # 도착했는데 남은 거리가 홀수면 목적지 도착 불가능
            return 'impossible'                                     # 이 조건문이 없어도 정상 작동하지만 있으면 더 빠르게 작동

        for key in direction:                                       # 명령어 사전순 사방위 순회
            nx = x + direction[key][0]
            ny = y + direction[key][1]
            new = command + key
            if 0 < nx <= n and 0 < ny <= m:                         # map을 벗어나지 않으면서
                if abs(nx - r) + abs(ny - c) + len(new) > k:        # (남은 거리 + 지금까지 온 거리)가 k 보다 크면 continue
                    continue
                q.append((nx, ny, new))                             # 사전순 첫 번째 명령어만 필요하므로 q에 추가 후 break
                break