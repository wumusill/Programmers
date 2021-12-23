# def solution(participant, completion):
#     answer = sorted(participant)
#     sort_completion = sorted(completion)
#     i = 0
#     while len(sort_completion) > 0:
#         if answer[i] == sort_completion[0]:
#             answer.pop(i)
#             sort_completion.pop(0)
#         else:
#             i += 1
#     return answer[0]

import collections

def solution(participant, completion):
    dict1 = collections.Counter(participant)
    dict2 = collections.Counter(completion)
    a = dict1 - dict2

    return list(a.keys())[0]


print(solution(['leo','kiki','eden'], ['eden', 'kiki']))
print(solution(['mari', 'jos', 'niko', 'vinko','filipa'], ['jos', 'filipa', 'mari', 'niko']))
print(solution(['mis','sta', 'mis', 'ana'], ['sta', 'ana', 'mis']))

