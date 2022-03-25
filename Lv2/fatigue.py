from itertools import permutations


def solution(k, dungeons):
    answer = []
    first = k
    nPr = permutations(dungeons)
    for case in nPr:
        k = first
        res = 0
        for needs, spend in case:
            if k < needs:
                break
            else:
                k -= spend
                res += 1
            answer.append(res)

    return max(answer)


print(solution(80, [[30, 10], [80, 20], [50, 40]]))

##############################################################################
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution_2(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer


print(solution_2(80, [[30, 10], [80, 20], [50, 40]]))