from math import gcd

def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]


# 유클리드 호제법 코드
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

