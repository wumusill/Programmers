def solution(n):
    if n % 2 == 0:
        return "수박" * (n // 2)
    else:
        return "수" + '박수' * (n // 2)


def solution_2(n):
    s = "수박" * n
    return s[:n]
