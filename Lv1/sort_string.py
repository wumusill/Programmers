def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))