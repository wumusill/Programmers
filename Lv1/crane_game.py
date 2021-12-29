from collections import deque

stack = deque()

def solution(board, moves):
    disappeard_times = 0
    catched = None
    for i in moves:
        for j in range(len(board)):
            catched = 0
            if board[j][i-1] == 0:
                continue
            elif board[j][i-1] != 0:
                catched = board[j][i-1]
                board[j][i-1] = 0
                break
        if catched == 0:
            continue
        if len(stack) == 0:
            stack.append(catched)
        else:
            if catched == stack[-1]:
                stack.pop()
                disappeard_times += 1
            else:
                stack.append(catched)
    return disappeard_times * 2

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1]
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))

def solution_2(board, moves):
    stacklist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                stacklist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer