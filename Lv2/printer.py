from collections import deque
import heapq


def solution(priorities, location):
    dq = deque()
    heap = []
    answer = 1

    for i in range(len(priorities)):
        dq.append((priorities[i], i))

    for i in range(len(priorities)):
        heapq.heappush(heap, -priorities[i])

    _max = -heapq.heappop(heap)
    while priorities:
        prior, idx = dq.popleft()
        if _max == prior:
            if idx == location:
                return answer
            _max = -heapq.heappop(heap)
            answer += 1
        dq.append((prior, idx))