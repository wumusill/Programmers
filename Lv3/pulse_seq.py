def solution(sequence):
    # 첫 데이터 기록
    l1 = [-sequence[0]]
    l2 = [sequence[0]]
    a = 1
    b = -1
    
    # 2번째 값부터 순회
    for i in range(1, len(sequence)):
        # 펄스 값 계산
        res1 = sequence[i] * a
        res2 = sequence[i] * b

        # 펄스 부분 수열 합계 구하기
        # (이전 합계에 더하기, 새로운 부분 수열 시작) 중 큰 값 기록
        res1 = max(l1[i-1] + res1, res1)
        res2 = max(l2[i-1] + res2, res2)
        l1.append(res1)
        l2.append(res2)

        # 새로운 펄스 값 계산 위해 스위치
        a, b = b, a

    # 가장 큰 펄스 부분 수열 합계 반환
    return max(max(l1), max(l2))