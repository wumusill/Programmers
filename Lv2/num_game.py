# n진수 게임
from collections import deque


def solution(n, t, m, p):
    answer = ''
    for i in range(t*m):
        if i < n:
            if i < 10:
                answer += str(i)
            else:
                if i == 10:
                    answer += 'A'
                elif i == 11:
                    answer += 'B'
                elif i == 12:
                    answer += 'C'
                elif i == 13:
                    answer += 'D'
                elif i == 14:
                    answer += 'E'
                elif i == 15:
                    answer += 'F'
        else:
            num = i
            mod_q = deque()
            while num != 0:
                mod = num % n
                if mod == 10:
                    mod = 'A'
                elif mod == 11:
                    mod = 'B'
                elif mod == 12:
                    mod = 'C'
                elif mod == 13:
                    mod = 'D'
                elif mod == 14:
                    mod = 'E'
                elif mod == 15:
                    mod = 'F'
                mod_q.appendleft(str(mod))
                num = num // n
            answer += ''.join(mod_q)
    return answer[(p - 1):m*t:m]


print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))