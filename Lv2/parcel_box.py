def solution(order):
    # 차에 실린 택배 개수
    answer = 0
    # 보조 벨트
    sub = []
    # 차에 실어야 하는 순서
    t = 0
    
    # 1부터 order의 길이 만큼 확인
    for i in range(1, len(order) + 1):
        # 만약 실어야하는 순서와 i가 같다면
        if i == order[t]:
            # 실은 후 개수 +1 & 다음 순서 확인하기 위해 t += 1
            answer += 1
            t += 1
        # 순서가 아니라면 보조 벨트에 올리기
        else:
            sub.append(i)
        
        # 보조 벨트에 물품이 있고 & 보조 벨트의 끝이랑 실어야하는 순서가 같다면
        while sub and sub[-1] == order[t]:
            # 보조 벨트 상자를 빼서 차에 실음
            answer += 1
            sub.pop()
            t += 1
    return answer 