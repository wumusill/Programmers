def dfs(queen, n, row):
    count = 0

    if n == row:
        return 1

    # 가로로 한번만 진행
    for x in range(n):
        queen[row] = x

        for y in range(row):
            # 세로로 겹치면 안됨
            if queen[y] == queen[row]:
                break

            # 대각선으로 겹치면 안됨
            if abs(queen[y] - queen[row]) == (row - y):
                break
        # 세로, 대각선이 겹치지 않는다면 dfs 이어서 진행
        else:
            count += dfs(queen, n, row + 1)

    return count


def solution(n):
    # index가 row이고 해당 value가 column
    # list에 같은 값이 있다는 것은 세로로 겹친다는 것
    queen = [0] * n

    return dfs(queen, n, 0)


print(solution(4))
print(solution(7))