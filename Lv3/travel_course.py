def recursion(route, n, now, visited):
    global answer
    # route의 길이가 정답의 길이와 같아지면 answer에 저장하고 재귀 종료
    if len(route) == n:
        answer.append(route)
        return
    else:
        if now in visited:                                         # 출발 가능 도시라면
            for next in visited[now]:                              # 도착지 순회
                if visited[now][next] > 0:                         # 도착지에 갈 수 있는 횟수가 남았다면
                    visited[now][next] -= 1                        # 횟수 차감하고
                    recursion(route + [next], n, next, visited)    # 재귀
                    visited[now][next] += 1                        # 재귀 종료 후 차감한 횟수 복원


def solution(tickets):
    global answer
    answer = []
    visited = {}

    # n : 정답 list의 길이
    n = len(tickets) + 1

    # ticket dictionary에 저장 : {출발지 :{도착지:횟수}
    # [[a, b], [a, c], [a, c] -> {a:{b:1, c:2}}
    for a, b in tickets:
        if a in visited:
            if b in visited[a]:
                visited[a][b] += 1
            else:
                visited[a][b] = 1
        else:
            visited[a] = {}
            visited[a][b] = 1

    # ICN 출발지 설정 후 재귀
    recursion(['ICN'], n, 'ICN', visited)

    # 가능한 경로 사전순 오름차순 정렬 후, 첫 번째 경로 반환
    answer.sort()
    return answer[0]