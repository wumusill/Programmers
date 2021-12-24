def solution(answers):
    answer = []
    len_answers = len(answers)
    repeat_1 = [1, 2, 3, 4, 5]
    repeat_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    repeat_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_1 = repeat_1 * (len_answers // len(repeat_1))
    answer_1 += repeat_1[:len_answers - len(answer_1)]

    answer_2 = repeat_2 * (len_answers // len(repeat_2))
    answer_2 += repeat_2[:len_answers - len(answer_2)]

    answer_3 = repeat_3 * (len_answers // len(repeat_3))
    answer_3 += repeat_3[:len_answers - len(answer_3)]

    score_1 = 0
    score_2 = 0
    score_3 = 0

    for i in range(len_answers):
        if answers[i] == answer_1[i]:
            score_1 += 1
        if answers[i] == answer_2[i]:
            score_2 += 1
        if answers[i] == answer_3[i]:
            score_3 += 1
    max_score = max(score_1, score_2, score_3)

    if score_1 == max_score:
        answer.append(1)
    if score_2 == max_score:
        answer.append(2)
    if score_3 == max_score:
        answer.append(3)

    return answer

# print(solution([1, 2, 3, 4, 5]))
# print(solution([1, 3, 2, 4, 2]))
print(solution([5, 4, 3, 2, 1, 5, 4, 3, 2, 1]))