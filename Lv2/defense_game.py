import heapq


def solution(n, k, enemy):
    answer = 0
    h = []
    for i in range(len(enemy)):
        # 라운드 클리어하기 위해 소모된 병사 기록
        n -= enemy[i]
        heapq.heappush(h, -enemy[i])

        # 병사가 남았다면 라운드 클리어
        if n >= 0:
            answer = i + 1
        # 병사가 모자라면
        else:
            # 가장 병사가 많이 소모된 라운드 무적권 사용하여 클리어 처리
            if k > 0:
                n -= heapq.heappop(h)
                k -= 1
                answer = i + 1
            # 무적권 사용불가, 이전 라운드까지 반환
            else:
                return i

    return answer
##########################################################################################################
import heapq as hq


def solution(n, k, enemy):
    # 무적권 개수만큼 힙 생성
    q = enemy[:k]
    hq.heapify(q)

    # 그 다음 라운드
    for idx in range(k,len(enemy)):
        # heappushpop : item을 push 한 뒤 pop, heappush(), heappop()을 하는 것보다 효율적으로 처리
        # 병사 소모가 가장 적은 순으로 라운드 클리어 처리
        n -= hq.heappushpop(q, enemy[idx])

        # 병사가 모자라면, 이전 라운드까지 반환
        if n < 0:
            return idx
    # 병사가 남거나 딱 맞으면 모두 클리어
    return len(enemy)