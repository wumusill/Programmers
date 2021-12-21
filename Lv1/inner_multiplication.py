def solution(a, b):
    l = []
    for i in range(len(a)):
        multi = a[i] * b[i]
        l.append(multi)
    return sum(l)


# def solution(a, b):
#     return sum([x * y for x, y in zip(a, b)])


# def solution(a, b):
#     answer = 0
#     for i, j in zip(a, b):
#         answer += i * j
#     return answer