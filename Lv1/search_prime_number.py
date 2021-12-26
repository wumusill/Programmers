# 첫 시도, 효율성 최악
def solution_1(n):
    sosu = 1
    for i in range(3, n+1, 2):
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            sosu += 1
    return sosu

# 두 번째 시도, 첫 시도 대비 효율성 상당히 개선, 여전히 효율성 통과 기준 미충족
def solution_2(n):
    sosu = [2]
    for i in range(3, n+1, 2):
        cnt = 0
        for j in sosu:
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            sosu.append(i)
    return len(sosu)

# 에라토스테네스의 체, 효율성 최고
def solution_3(n):
    l = [True] * (n+1)
    sosu = 0
    for i in range(2, n+1):
        if l[i]:
            for j in range(2*i, n+1, i):
                l[j] = False
    for _ in range(2, n+1):
        if l[_]:
            sosu += 1
    return sosu

# 에라토스테네스의 체를 이용한 다른 풀이
def solution(n):
    num = set(range(2, n+1))

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)