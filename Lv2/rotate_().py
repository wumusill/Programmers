from collections import deque

# 올바른 괄호인지 판별하는 함수
def judge(s):
    d = {']': '[', ')': '(', '}': '{'}
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == ']' and stack[-1] == d[i]:
                stack.pop()
            elif i == '}' and stack[-1] == d[i]:
                stack.pop()
            elif i == ')' and stack[-1] == d[i]:
                stack.pop()
            else:
                stack.append(i)
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate()              # 문자열 회전
        if judge(s):            # 올바른 괄호인지 판단
            answer += 1
    return answer