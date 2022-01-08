def solution(sizes):
    l = list(sizes)
    h_l = []
    v_l = []

    for x, y in l:
        if x < y:
            x, y = y, x
        h_l.append(x)
        v_l.append(y)

    h = max(h_l)
    v = max(v_l)

    return h * v

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))


def solution_2(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)