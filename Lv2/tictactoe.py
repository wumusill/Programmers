def solution(board):
    cases = [
            # 가로
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],
            
            # 세로
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],
            
            # 대각
            [[0, 0], [1, 1], [2, 2]],
            [[0, 2], [1, 1], [2, 0]],
        ]
    count_o = 0
    count_x = 0
    for row in board:
        count_o += row.count("O")
        count_x += row.count("X")
    
    # o 차례인데 x를 놓은 경우
    if count_x > count_o:
        return 0
    
    # o가 이겼는데 x를 놓은 경우
    elif count_x == count_o:
        for a, b, c in cases:
            if board[a[0]][a[1]] == "O" and board[b[0]][b[1]] == "O" and board[c[0]][c[1]] == "O": 
                return 0
    
    elif count_x < count_o:
        # x 차례인데 o를 놓은 경우
        if count_o - count_x != 1:
            return 0
        
        # x가 이겼는데 o를 놓은 경우
        for a, b, c in cases:
            if board[a[0]][a[1]] == "X" and board[b[0]][b[1]] == "X" and board[c[0]][c[1]] == "X": 
                return 0
    return 1