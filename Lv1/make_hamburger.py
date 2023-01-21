def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) > 3:
            if (stack[-1] == 1) & (stack[-2] == 3) & (stack[-3] == 2) & (stack[-4] == 1):
                for _ in range(4):
                    stack.pop()
                answer += 1
    return answer