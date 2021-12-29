def solution(n):
    s = 0
    for i in range(1, n+1):
        if n % i == 0:
            s += i
    return s


def solution_2(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])