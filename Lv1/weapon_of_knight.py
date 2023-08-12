def solution(number, limit, power):
    answer = 0
    # 0부터 number 까지 약수의 개수를 기록할 리스트
    cnt_list = [0 for i in range(number + 1)]

    # 약수 기록하는 반복문
    for i in range(1, number + 1):
        for j in range(1, int(i ** 0.5) + 1):
            # 약수인데
            if i % j == 0:
                # 제곱수면 1만 더하고
                if j ** 2 == i:
                    cnt_list[i] += 1
                # 제곱수가 아니면 2를 더함
                else:
                    cnt_list[i] += 2
    
    # 약수의 개수가 limit을 초과하는지 체크
    for i in range(1, number + 1):
        if cnt_list[i] <= limit:
            answer += cnt_list[i]
        else:
            answer += power

    return answer