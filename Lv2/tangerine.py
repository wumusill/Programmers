from collections import Counter

def solution(k, tangerine):
    answer = 0
    s = 0
    cnt = sorted(Counter(tangerine).items(), key=lambda item: item[1]) 
    while s < k:
        res = cnt.pop()
        s += res[1]
        answer += 1
    return answer