from collections import Counter

def solution(N, stages):
    counter_list = Counter(stages)
    user_num = len(stages)
    rate_dict = {}

    for level in range(1, N+1):
        if user_num == 0:
            rate_dict[level] = 0
        else:
            rate_dict[level] = counter_list[level] / user_num
            user_num -= counter_list[level]

    rate_dict_ = sorted(rate_dict.items(), reverse=True, key=lambda item: (item[1], -item[0]))

    answer_list = []
    for i in rate_dict_:
        answer_list.append(i[0])
    return answer_list


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(1, [2]))
print(solution(5, [3, 3, 3, 3, 3]))