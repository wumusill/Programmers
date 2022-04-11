import heapq

def solution(operations):
    answer = [0, 0]

    min_heap = []
    max_heap = []

    for i in operations:
        command, num = i.split()

        if command == 'I':
            heapq.heappush(min_heap, int(num))
            heapq.heappush(max_heap, (-int(num), int(num)))
        elif command == 'D':
            if min_heap:
                if num == '-1':
                    heapq.heappop(min_heap)
                    max_heap.pop()
                else:
                    heapq.heappop(max_heap)
                    min_heap.pop()
    if min_heap:
        answer[0] = max_heap[0][1]
        answer[1] = min_heap[0]

    return answer


print(solution(["I 16", "D 1"]))
print(solution(['I 7', 'I 5', 'I -5', 'D -1']))
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))