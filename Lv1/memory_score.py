def solution(name, yearning, photo):
    answer = []
    score = {}

    # 이름에 대응되는 점수 기록하는 사전
    for n, s in zip(name, yearning):
        score[n] = s
    
    # 사진 하나씩 순회
    for p in photo:
        # 점수를 기록
        res = 0
        # 사진 속 이름 하나씩 순회
        for name in p:
            # 만약 이름이 점수 사전에 있다면 더하기
            if name in score:
                res += score[name]
        # 점수 합계 기록
        answer.append(res)
        
    return answer