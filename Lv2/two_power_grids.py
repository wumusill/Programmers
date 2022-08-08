# 하나의 전력망을 끊은 후 dfs를 통해 개수 파악, 최소 차이 출력
from collections import deque


def solution(n, wires):
    cut = 0
    answer = int(1e9)
    for _ in range(n - 1):
        # n개의 노드, n - 1개의 연결 입력을 위한 초기 세팅
        stack = deque()
        connect = [[] for _ in range(n + 1)]
        visited = [False] * (n + 1)
        cnt_a = 1
        for i in range(n - 1):
            # 하나의 연결을 끊은 후 graph 세팅
            if i == cut:
                continue
            u, v = wires[i]
            connect[u].append(v)
            connect[v].append(u)

        # 1부터 n까지의 노드 dfs, t의 역할은 아래에
        t = 0
        for a in range(1, n + 1):
            # 첫 방문 노드, 연결된 노드가 있다면 방문 처리 후 stack append
            if connect[a]:
                visited[a] = True
                stack.append(a)
            # 첫 방문 노드에 대한 dfs 실행
            while stack:
                x = stack.pop()
                for b in connect[x]:
                    if not visited[b]:
                        visited[b] = True
                        stack.append(b)
                        # 첫 방문 노드와 연결된 노드라면 count
                        if t == 0:
                            cnt_a += 1
            # while문으로 첫 방문 노드와 연결된 노드를 모두 파악
            # 다시 for문으로 첫 방문 노드와 연결되지 않은 전력망 방문 시 count 되지 않도록 처리
            t += 1

        # 다른 전력망의 노드 개수는 (전체 노드 - count 된 노드)
        cnt_b = n - cnt_a
        # 다시 첫 for문으로 돌아가 다른 연결 끊기
        cut += 1
        # 정답은 두 전력망 노드의 개수 차가 가장 작은 경우
        answer = min(answer, abs(cnt_a - cnt_b))

    return answer