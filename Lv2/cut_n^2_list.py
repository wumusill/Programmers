def solution(n, left, right):
    # 1부터 n까지의 list
    l = [i for i in range(1, n + 1)]
    answer = []

    l_times = left // n # 1
    l_rest = left % n   # 1
    r_times = right // n # 1
    r_rest = right % n  # 2

    # 시작 값은 (l_times + 1)번 째 list의 l_rest index
    # l_times보다 작은 index의 값은 l[l_times]의 값과 같음
    # n = 4일 때
    # 몫이 1이라면 [2, 2, 3, 4] / 2라면 [3, 3, 3, 4]
    for i in range(n):
        if i < l_times:
            l[i] = l[l_times]
        # 마지막 list가 첫 list와 다른 순서여야만 l_rest의 뒷 값 모두 추가
        if l_times != r_times:
            if i >= l_rest:
                answer.append(l[i])
        # 마지막 list와 같은 순서라면 index가 r_rest보다는 작거나 같아야 함
        else:
            if i >= l_rest and i <= r_rest:
                answer.append(l[i])

    # l_times 다음 list부터 r_times 이전 list까지의 값을 모두 append
    for t in range(l_times + 1, r_times):
        # p번 째 list, list[p] 이전의 값은 list[p]의 값과 같음
        for k in range(n):
            if k < t:
                answer.append(l[t])
            else:
                answer.append(l[k])

    # 마지막 list가 첫 list와 같은 순서라면 실행되서는 안되는 구문
    if l_times != r_times:
        # 마지막 list r_rest index까지 append
        for j in range(n):
            if j < r_times:
                l[j] = l[r_times]
            if j <= r_rest:
                answer.append(l[j])

    return answer


print(solution(3, 2, 5)) # [3, 2, 2, 3]
print(solution(4, 7, 14)) # [4, 3, 3, 3, 4, 4, 4, 4]
print(solution(3, 4, 5)) # [2, 3]
print(solution(3, 3, 4)) # [2, 2]
# [1, 2, 3,  2, 2, 3,  3, 3, 3]

# 규칙은 이렇게 찾는거다 모자란놈 #####################################################
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        a = i // n
        b = i % n
        if a < b:
            a, b = b, a
        answer.append(a + 1)

    return answer