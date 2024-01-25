from collections import Counter


def solution(weights):
    answer = 0

    # 무게 개수
    counter = Counter(weights)

    # 개수가 2개 이상이면 조합 계산
    for k in counter:
        if counter[k] > 1:
            answer += counter[k] * (counter[k] - 1) / 2

    # 중복 제거 후 순회
    # 비율 (1:2, 2:3, 3:4)에 해당하는 무게가 있으면
    # 만들 수 있는 조합 계산
    weights = set(weights)
    for w in weights:
        for case in [w * 2, w / 2 * 3, w / 3 * 4]:
            if case in counter:
                answer += counter[case] * counter[w]

    return answer