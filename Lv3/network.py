# 미완
def dfs(graph, v):
    visited[n] = True
    i = 0
    for i in graph[v]:
        if visited[i] == False:
            visited[n] = True
            i += 1
            dfs(i)

def solution(n, computers):
    answer = n
    computers





visited = [False] * (n+1)

a = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

b = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]