from collections import deque


def solution(people, limit):
    answer = 0
    deq = deque(sorted(people))
    while deq:
        if len(deq) == 1:
            answer += 1
            break
        if deq[0] + deq[-1] <= limit:
            deq.pop()
            deq.popleft()
        else:
            deq.pop()
        answer += 1
    return answer


print(solution([70, 50, 80, 50], 100))
# print(solution([70, 80, 50], 100))
# print(solution([40, 60, 40, 60], 100))
# print(solution([40, 40, 40, 60, 60], 120))