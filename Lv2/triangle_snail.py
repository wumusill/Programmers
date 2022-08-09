# 움직이는 방향은 아래, 오른쪽 위 3 방향

def solution(n):
    answer = []
    triangle = [[0] * n for _ in range(n)]
    x, y = -1, 0
    res = 1

    for i in range(n):
        for j in range(i, n):
            # 아래로 내려감
            if i % 3 == 0:
                x += 1
            # 오른쪽으로 채워 나감
            elif i % 3 == 1:
                y += 1
            # 위로 올라감
            elif i % 3 == 2:
                x -= 1
                y -= 1

            triangle[x][y] = res
            res += 1

    for li in triangle:
        for element in li:
            if element != 0:
                answer.append(element)

    return answer


print(solution(4))
print(solution(5))
print(solution(6))