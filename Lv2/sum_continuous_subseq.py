# 투포인터 접근
def solution(sequence, k):
    # 왼쪽 포인터
    left = 0
    # 오른쪽 포인터
    right = 0
    answer = []
    res = sequence[0]
    
    while True:
        # 연속 부분 수열의 합이 목표 값보다 작은데
        # 오른쪽 포인터 뒤에 숫자가 더 있다면
        # 오른쪽 포인터를 한 칸 뒤로 이동
        if res < k and right < len(sequence) - 1:
            right += 1
            res += sequence[right]

        # 연속 부분 수열의 합이 목표 값과 같다면
        # 왼쪽 포인터, 오른쪽 포인터, 두 포인터 사이의 거리를 기록
        # 왼쪽 포인터 뒤로 한 칸 이동
        elif res == k:
            answer.append([left, right, right - left])
            res -= sequence[left]
            left += 1

        # 연속 부분 수열의 합이 목표 값보다 크다면
        # 왼쪽 포인터를 뒤로 한 칸 이동
        elif res > k:
            res -= sequence[left]
            left += 1

        # 만약 연속 부분 수열의 합이 목표 값보다 작은데
        # 오른쪽 포인터 뒤에 숫자가 더 없다면 반복문 종료
        if res < k and right == len(sequence) - 1:
            break
    
    # 두 포인터 사이 거리를 기준으로 오름차순 정렬
    answer.sort(key=lambda x: x[2])

    # 두 포인터 사이 거리가 가장 가까운 쌍을 출력
    return [answer[0][0], answer[0][1]]