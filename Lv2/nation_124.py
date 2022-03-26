def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(11))
print(solution(12))
print(solution(13))
print(solution(14))