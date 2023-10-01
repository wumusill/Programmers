def solution(targets):
    answer = 0

    # end 기준 오름차순 정렬
    targets.sort(key=lambda x: x[1])

    # 가장 작은 end 부터 순회
    # 만약 다음 start가 이전 end보다 작다면 아무 문제 없음, 이전 요격 시스템으로 충분
    # 그러나 다음 start가 이전 end보다 크거나 같으면 요격 시스템 하나 추가로 필요
    now = 0
    for i in range(len(targets)):
        next = targets[i][0]
        if now <= next:
            answer += 1
            now = targets[i][1]
    return answer