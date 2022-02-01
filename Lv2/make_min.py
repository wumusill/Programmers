def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer

print(solution([1, 4, 2], [5, 4, 4]))
print(solution([1, 2], [3, 4]))