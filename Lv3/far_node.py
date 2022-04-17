from collections import deque

def solution(n, edge):
    queue = deque()
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)

    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    queue.append(1)
    visited[1] = True

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[a] + 1

    return distance.count(max(distance))


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))