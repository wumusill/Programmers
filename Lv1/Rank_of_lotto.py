def solution(lottos, win_nums):
    num_of_zeros = lottos.count(0)
    win_num = 0
    for i in lottos:
        if i in win_nums:
            win_num += 1

    if win_num == 6:
        return [1, 1]
    elif win_num == 5:
        return [2 - num_of_zeros, 2]
    elif win_num == 4:
        return [3 - num_of_zeros, 3]
    elif win_num == 3:
        return [4 - num_of_zeros, 4]
    elif win_num == 2:
        return [5 - num_of_zeros, 5]
    elif win_num == 1:
        return [6 - num_of_zeros, 6]
    elif win_num == 0:
        if num_of_zeros == 0:
            return [6, 6]
        return [7 - num_of_zeros, 6]


# def solution(lottos, win_nums):
#     rank = [6, 6, 5, 4, 3, 2, 1]
#
#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans], rank[ans]