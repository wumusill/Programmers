from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])
    while queue:
        s, l = queue.popleft()
        if l > len(numbers):
            break
        if l == len(numbers) and s == target:
            answer += 1
        queue.append((s+numbers[l-1], l+1))
        queue.append((s-numbers[l-1], l+1))

    return answer


print(solution([1, 1, 1, 1, 1], 3))

#########################################################################
from itertools import product


def solution_2(numbers, target):
    l = [(x, -x) for x in numbers]
    # l 앞에 * 을 안쓰면
    # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
    # *를 쓰면 왜 에러가 안나지 무슨 역할
    s = list(map(sum, product(*l)))
    return s.count(target)


print(solution_2([1, 1, 1, 1, 1], 3))
#########################################################################
from collections import deque


def solution(distance, scope, times):
    # scope = deque(scope)
    # times = deque(times)
    dq = deque()

    for i in range(len(scope)):
        scope[i].sort()
        dq.append([*scope[i], *times[i]])
        scope[i].append(i)
        times[i].append(i)

    dq = sorted(dq, key=lambda x: -x[0])

    answer = 0

    # 1, 2,      3, 4, 5, 6, 7
    while True:
        if dq[-1][0] == answer:
            start, end, work, rest = dq.pop()
            while answer <= end:
                if 1 <= answer % (work + rest) <= work:
                    return answer
                else:
                    answer += 1
        else:
            answer += 1

    return answer

    # 1, 2, (3, 4), (5, 6, 7, 8), 9, 10

#########################################################################
# 승후의 재귀 풀이
def solution(numbers, target):
    answer = 0
    def inner(index, result):
        if index == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            inner(index+1, result+numbers[index])
            inner(index+1, result-numbers[index])
    inner(0,0)
    return answer