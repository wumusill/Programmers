# 아이디어
# y에서 -n, /2, /3 해서 몇 번의 계산 후에 x를 찾아가는지 확인
from collections import deque

def solution(x, y, n):
    # 탐색 전 방문 여부와 queue 세팅
    q = deque([(y, 0)])
    v = [-1] * (y + 1)

    # q에 원소가 있다면
    while q:
        ny, times = q.popleft()
        if ny == x:
            return times
        
        # 1 <= x <= y <= 1,000,000
        # 0보다 작으면 x를 찾아갈 수 없으므로 return -1
        if ny <= 0:
            return -1
        
        # -n 방문
        a = ny - n
        if v[a] == -1:
            q.append((a, times + 1))
            v[a] = times + 1

        # 2로 나누어 떨어질 때만 /2 방문
        if ny % 2 == 0:
            b = ny // 2
            if v[b] == -1:
                q.append((b, times + 1))
                v[b] = times + 1
        
        # 3으로 나누어 떨어질 때만 /3 방문
        if ny % 3 == 0:
            c = ny // 3
            if v[c] == -1:
                q.append((c, times + 1))
                v[c] = times + 1