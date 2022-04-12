import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) >= 2:
            min_scoville = heapq.heappop(scoville)
            second_scoville = heapq.heappop(scoville)
            if min_scoville >= K:
                return answer

            heapq.heappush(scoville, second_scoville * 2 + min_scoville)
            answer += 1
        else:
            min_scoville = heapq.heappop(scoville)
            if min_scoville < K:
                return -1
            return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 7))