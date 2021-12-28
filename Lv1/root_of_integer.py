def solution(n):
    root_n = n ** 0.5
    decimal_of_root_n = root_n % 1
    if decimal_of_root_n == 0:
        return int((root_n + 1) ** 2)
    else:
        return -1



print(solution(121))
print(solution(3))