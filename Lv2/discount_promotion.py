from collections import Counter

def solution(want, number, discount):
    answer = 0
    d = {}
    for key, val in zip(want, number):
        d[key] = val
    
    for i in range(len(discount) - 9):
        dis = Counter(discount[i:i+10])
        if dis == d:
            answer += 1
            
    return answer 