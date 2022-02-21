def solution(brown, yellow):
    area = brown + yellow
    for w in range(1, int(area ** 0.5) + 1):
        if area % w == 0:
            h = area // w
        if (h - 2) * (w - 2) == yellow:
            return [h, w]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))