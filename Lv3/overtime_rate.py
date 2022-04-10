import heapq


def solution(n, works):
    answer = 0
    heap = []

    for i in works:
        heapq.heappush(heap, (-i, i))

    for j in range(n):
        largest = heapq.heappop(heap)[1]
        heapq.heappush(heap, (-(largest - 1), largest - 1))

    while heap:
        num = heapq.heappop(heap)[1]
        if num < 0:
            continue
        answer += num ** 2

    return answer


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))