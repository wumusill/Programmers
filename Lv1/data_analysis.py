def solution(data, ext, val_ext, sort_by):
    answer = []
    
    d = {'code':0, 'date':1, 'maximum':2, 'remain':3}
    key = d[ext]
    
    for sample in data:
        if sample[key] <= val_ext:
            answer.append(sample)
    
    answer.sort(key=lambda x: x[d[sort_by]])
    
    return answer