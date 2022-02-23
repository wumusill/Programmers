def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    while n != 1:
        x = s // n
        answer.append(x)
        s -= x
        n -= 1
    answer.append(s)
    return sorted(answer)


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))