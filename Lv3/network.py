def solution_with_recursion(n, computers):
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

################################################################################
def solution_with_stack(n, computers):
    visited = [False] * n
    stack = []
    answer = n

    for computer in computers:
        for i in range(n):
            if computer[i] == 1 and visited[i] == False:
                stack.append(i)
                visited[i] = True
            while stack:
                com = stack.pop()
                for j in range(0, n):
                    if visited[j] == False and computers[com][j] == 1:
                        visited[j] = True
                        stack.append(j)
                        answer -= 1
    return answer


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

print(solution_with_stack(3, a)) # 2
print(solution_with_recursion(3, b)) # 1
print(solution_with_stack(4, c))