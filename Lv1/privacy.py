import datetime as dt

def solution(today, terms, privacies):
    answer = []
    y1, m1, d1 = map(int, today.split("."))
    splited_privacies = map(lambda x: x.split(), privacies)
    
    # 약관별 저장 개월 수 저장
    delete_dict = {}
    for val in terms:
        lv, month = val.split()
        delete_dict[lv] = int(month)
        
    for idx, privacy in enumerate(splited_privacies):
        date = privacy[0]
        grade = privacy[1]
        y2, m2, d2 = map(int, date.split("."))
        
        # 월 연산
        m2 += delete_dict[grade]
        
        # 12보다 크다면 연 올림
        # 유효기간이 12보다 클 수 있으므로 while문으로 연산
        while m2 > 12:
            y2 += 1
            m2 -= 12
        
        # date 비교 연산
        a = dt.date(y1, m1, d1)
        b = dt.date(y2, m2, d2)
    
        if a >= b:
            answer.append(idx + 1)

    return answer