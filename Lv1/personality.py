def solution(survey, choices):
    answer = ''

    # 점수 기록지
    score = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    # 점수 기록
    for case, choice in zip(survey, choices):
        a, b = case[0], case[1]
        if choice == 1:
            score[a] += 3
        elif choice == 2:
            score[a] += 2
        elif choice == 3:
            score[a] += 1
        elif choice == 5:
            score[b] += 1
        elif choice == 6:
            score[b] += 2
        elif choice == 7:
            score[b] += 3

    # 더 높은 점수 기록, 동률일 경우 알파벳 사전 순 더 빠른 것 입력
    for a, b in [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]:
        if score[a] < score[b]:
            answer += b
        elif score[a] >= score[b]:
            answer += a

    return answer