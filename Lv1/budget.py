def solution(d, budget):
    d.sort()
    for i in range(1, len(d) + 1):
        a = d[:i]
        if sum(a) > budget:
            return i - 1
        elif sum(a) == budget:
            return i
    return i


print(solution([1, 3, 2, 5, 4], 9))
print(solution([2, 2, 3, 3], 10))