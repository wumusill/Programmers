def solution(m, n, board):
    answer = 0

    # 행 문자열 분리
    for i in range(m):
        board[i] = list(board[i])

    # 알파벳 숫자로 치환
    val = 1
    d = {}
    for i in range(m):
        for j in range(n):
            key = board[i][j]
            if key not in d:
                d[key] = val
                val += 1
            board[i][j] = d[key]

    # 시계방향 90도 회전
    turned = [[] for _ in range(n)]
    for i in range(-1, -m - 1, -1):
        for j in range(n):
            turned[j].append(board[i][j])

    # 제거해야 하는 숫자 좌표 저장
    while True:
        will_del = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if turned[i][j] == 0:
                    continue
                if turned[i][j] == turned[i + 1][j] == turned[i][j + 1] == turned[i + 1][j + 1]:
                    will_del.add((i, j))
                    will_del.add((i + 1, j))
                    will_del.add((i, j + 1))
                    will_del.add((i + 1, j + 1))

        # 제거해야 할 좌표 0으로 대치 -> 삭제 처리
        # 삭제한 블록 개수 갱신
        if len(will_del) > 0:
            answer += len(will_del)
            for i, j in will_del:
                turned[i][j] = 0

            # 0 우측으로 몰기
            temp = []
            for i in range(n):
                for j in range(m):
                    res = turned[i].pop(0)
                    if res == 0:
                        temp.append(res)
                    else:
                        turned[i].append(res)
                while temp:
                    turned[i].append(temp.pop())

        # 제거할 요소 없으면 while문 탈출
        else:
            break

    return answer