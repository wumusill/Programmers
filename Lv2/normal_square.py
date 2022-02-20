from math import gcd


def solution(w, h):
    _gcd = gcd(w, h)
    _w = w / _gcd
    _h = h / _gcd

    answer = w * h - (_w + _h - 1) * _gcd

    return answer

print(solution(8, 12))

# 최대공약수가 1일 때 직선이 지나는 점이 없다
# 이 때 대각선이 지나는 가로와 세로의 개수만큼 사각형이 갈라진다
# 처음 시작하는 사각형 1개를 빼준다