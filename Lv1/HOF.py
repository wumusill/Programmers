def solution(k, score):
    answer = []
    lb = []
    for score in score:
        lb.append(score)
        lb.sort()
        if len(lb) > k:
            lb.pop(0)
        answer.append(lb[0])
            
    return answer 