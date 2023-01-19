# 시간초과 코드
# 매번 출발지에서 도착지까지의 거리를 반복문으로 확인
from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    q = deque()
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[b].append(a)
        graph[a].append(b)
        
    for i in sources:
        visited = [-1] * (n + 1)
        visited[i] = 0
        q.append((i, 0))
        while q:
            now, dist = q.popleft()
            for j in graph[now]:
                if visited[j] == -1:
                    visited[j] = dist + 1
                    q.append((j, dist + 1))
                    
        answer.append(visited[destination])
        
    return answer


####################################################################################
# 정답
# 도착지에서 시작하여 출발지까지의 거리 한번만 계산

from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    q = deque()
    graph = [[] for _ in range(n + 1)]
    
    for a, b in roads:
        graph[b].append(a)
        graph[a].append(b)
        
    visited = [-1] * (n + 1)
    visited[destination] = 0
    q.append((destination, 0))
    while q:
        now, dist = q.popleft()
        for j in graph[now]:
            if visited[j] == -1:
                visited[j] = dist + 1
                q.append((j, dist + 1))

    for s in sources:
        answer.append(visited[s])
        
    return answer