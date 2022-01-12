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

from itertools import product

def solution_2(numbers, target):
    l = [(x, -x) for x in numbers]
    # l 앞에 * 을 안쓰면
    # TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
    # *를 쓰면 왜 에러가 안나지 무슨 역할
    s = list(map(sum, product(*l)))
    return s.count(target)

print(solution_2([1, 1, 1, 1, 1], 3))