def solution(n, times):
    start = 1
    end = max(times) * n
    answer = 0
    while start <= end:
        result = 0
        mid = (start + end) // 2
        for i in times:
            result += mid // i

        if result < n:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer

print(solution(6, [7, 10]))