from itertools import combinations

def solution(numbers):
    nCr = combinations(numbers, 2)
    l = list(set(([sum(i) for i in nCr])))
    l.sort()
    return l


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
print(solution([100, 100, 99]))