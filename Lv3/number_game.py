# B가 A를 최대한 많이 이기려면 A보다 큰 숫자의 카드를 제시하되, 그 차이를 최소화 해야 함
from collections import deque


def solution(A, B):
    answer = 0
    A.sort(), B.sort()                  # A와 B 오름차순 정렬
    A, B = deque(A), deque(B)

    for i in range(len(A)):
        if A[0] < B[0]:                 # 현재 B의 최솟값이 A의 최솟값보다 크다면 이김
            A.popleft(), B.popleft()
            answer += 1
        else:                           # 아니면 졌으니 다음으로 큰 B카드 확인
            B.popleft()

    return answer