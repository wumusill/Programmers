def solution(board, h, w):
    answer = 0
    color = board[h][w]
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nh, nw = h + dx, w + dy
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]) and board[nh][nw] == color:
            answer += 1

    return answer