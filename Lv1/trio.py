from itertools import combinations

def solution(number):
    answer = 0
    nc3 = combinations(number, 3)
    for i in nc3:
        if sum(i) == 0:
            answer += 1
    return answer