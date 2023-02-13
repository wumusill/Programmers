def solution(numbers):
    # res에 자기 자신과 뒤 큰 수를 (자신, 뒤 큰 수)로 저장
    # 마지막 수는 무조건 -1이므로 -1과 함께 튜플로 저장
    res = [(numbers[-1], -1)]
    
    # numbers를 뒤집어서 뒤 부터 확인
    re_num = list(reversed(numbers))
    
    # 마지막 수는 처리해줬으므로 1부터 확인
    for i in range(1, len(numbers)):
        
        # 바로 이전 수가 현재보다 크다면, 그 수를 뒤 큰 수로 하여 저장
        if res[i-1][0] > re_num[i]:
            res.append((re_num[i], res[i-1][0]))
        
        # 바로 이전 수가 현재랑 같다면, 이전 수가 저장하고 있는 뒤 큰 수를 저장
        elif res[i-1][0] == re_num[i]:
            res.append((re_num[i], res[i-1][1]))
        
        # 바로 이전 수가 현재보다 작다면
        elif res[i-1][0] < re_num[i]:
            # 이전 수가 저장하고 있는 뒤 큰 수 보다 크다면 -1 저장
            if res[i-1][1] < re_num[i]:
                res.append((re_num[i], -1))
            # 이전 수가 저장하고 있는 뒤 큰 수 보다 작다면 이전 수의 뒤 큰 수 저장
            else:
                res.append((re_num[i], res[i-1][1]))
      
    # 뒤에서 부터 하나씩 꺼내서 뒤 큰 수만 answer에 추가
    answer = []
    for _ in range(len(res)):
        num, m = res.pop()
        answer.append(m)
    return answer

# 틀린 코드 그러나 어떤 반례가 있을까
########################################################################################            
# 정답 코드

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    # 인덱스를 하나씩 탐색
    for i in range(len(numbers)):

        # 스택에 인덱스가 있을 때
        # 현재 탐색 중인 인덱스의 숫자보다 스택 가장 위에 있는 인덱스의 숫자가 작다면
        while stack and numbers[stack[-1]] < numbers[i]:
            # 그 인덱스를 삭제하고
            idx = stack.pop()
            # 해당 인덱스의 뒤 큰 수를 현재 탐색 중인 숫자로 저장
            answer[idx] = numbers[i]
        
        # 인덱스를 스택에 추가
        stack.append(i)
    return answer