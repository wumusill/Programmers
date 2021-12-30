def solution(n):
    return list(map(int, list(str(n)[::-1])))

print(solution(12345))
print(solution(1234))
print(solution(29732))
print(solution(4857823))