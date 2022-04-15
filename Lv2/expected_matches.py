def solution(n, a, b):
    answer = 0
    while True:
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        answer += 1
        if a == b:
            break
    return answer


print(solution(8, 1, 7))    # 3
print(solution(16, 4, 5))   # 3
print(solution(8, 1, 2))    # 1
print(solution(8, 4, 7))    # 3
print(solution(16, 4, 8))   # 3