def solution(n, computers):
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i, visited)
            answer += 1
    return answer


def dfs(n, computers, i, visited):
    visited[i] = True
    for j in range(n):
        if i != j and computers[i][j] == 1 and visited[j] == False:
            dfs(n, computers, j, visited)

c = [
    [1, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 1]
]


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

print(solution(3, a)) # 2
print(solution(3, b)) # 1
print(solution(4, c))