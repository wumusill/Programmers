import heapq

def solution(N, road, K):
    answer = 0

    # 그래프와 거리를 기록할 리스트
    graph = [[] for _ in range(N + 1)]
    distance = [int(1e9)] * (N + 1)

    # 그래프 양방향 연결
    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    
    # 출발지(1번 노드) 힙에 삽입(거리, 노드)하고 1번 노드까지 거리는 0 
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))

    while q:
        dist, now = heapq.heappop(q)
        # 현재 탐색 중인 노드와 연결된 노드와 거리 탐색
        for b, c in graph[now]:
            # 1번 노드에서 연결된 노드까지의 거리 계산
            cost = dist + c
            # 거리가 기존에 기록된 거리보다 작으면 갱신하고 힙에 삽입
            if cost < distance[b]:
                distance[b] = cost
                heapq.heappush(q, (cost, b))

    # 기록된 거리 순회해서 K보다 작은 노드의 개수 계산
    for dist in distance[1:]:
        if dist <= K:
            answer += 1
            
    return answer