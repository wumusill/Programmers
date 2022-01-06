def solution(num):
    if num == 1:
        return 0
    else:
        for i in range(500):
            if num % 2 == 0:
                num /= 2
            else:
                num = num * 3 + 1
            if num == 1:
                return i + 1
    return -1

print(solution(6))
print(solution(16))
print(solution(626331))
print(solution(1))