def solution(n):
    l = [0] * (n+1)
    l[1] = 1
    for i in range(2, n+1):
        l[i] = (l[i-2] % 1234567 + l[i-1] % 1234567) % 1234567
    return l[-1]


print(solution(3))
print(solution(5))
print(solution(100))