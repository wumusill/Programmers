# 완전 탐색
def solution(wallpaper):
    a = 51
    b = 51
    c = 0
    d = 0
    for i, x in enumerate(wallpaper):
        if "#" in x:
            a = min(i, a)
            b = min(x.index("#"), b)
            c = max(i + 1, c)
            for j, y in enumerate(x):
                if y == "#":
                    d = max(j + 1, d)
    return [a, b, c, d]