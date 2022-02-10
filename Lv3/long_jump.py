l = [0] * 2001
l[0] = 1
l[1] = 1
for i in range(2, 2001):
    l[i] = l[i-1] + l[i-2]

def solution(n):
    return l[n] % 1234567

print(solution(4))
print(solution(3))