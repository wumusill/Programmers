from math import gcd


def solution(arr):
    arr.sort()
    answer = arr[0] * arr[1] // gcd(arr[0], arr[1])

    for i in range(2, len(arr)):
        answer = answer * arr[i] // gcd(answer, arr[i])

    return answer

print(solution([2, 6, 8, 14]))
print(solution([1, 2, 3]))
