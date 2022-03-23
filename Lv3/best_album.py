def solution(genres, plays):
    answer = []
    dict_index = {}
    dict_sum = {}
    l_keys = []
    for genre, play in zip(genres, enumerate(plays)):
        if genre in dict_index.keys():
            dict_index[genre] += [play]
            dict_sum[genre] += play[1]
        else:
            dict_index[genre] = [play]
            dict_sum[genre] = play[1]

    dict_sum = sorted(dict_sum.items(), key=lambda x: x[1], reverse=True)
    for i in dict_sum:
        l_keys.append(i[0])
    for key in l_keys:
        values = dict_index[key]
        values.sort(key=lambda x: (x[1], -x[0]), reverse=True)
        if len(values) >= 2:
            for i in range(2):
                answer.append(values[i][0])
        else:
            for i in range(len(values)):
                answer.append(values[i][0])
    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))
# [4, 1, 3, 0]
print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 500, 500, 500, 500]))
# [0, 2, 1, 4]