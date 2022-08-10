def solution(board):
    length = 0
    dp = board

    for x in range(1, len(board)):
        for y in range(1, len(board[0])):
            if dp[x][y] == 1:
                dp[x][y] = min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1

    for l in dp:
        length = max(length, max(l))

    return length ** 2


print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))