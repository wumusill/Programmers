def solution(n, lost, reserve):
    l = set(lost) - set(reserve)
    r = set(reserve) - set(lost)
    for i in r:
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)

    return n - len(l)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(5, [2, 4], [1, 3]))
