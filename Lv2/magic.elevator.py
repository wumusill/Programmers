from collections import deque

def solution(storey):
    answer = 0
    
    l = deque(map(int, list(str(storey))))
    
    # 맨 앞자리 올림 여부를 판단하기 위해 앞에 0 추가
    l.appendleft(0)
    
    # 하나 임의로 추가했기 때문에 - 1
    for _ in range(len(l) - 1):
        last_num = l.pop()
        
        # 6, 7, 8, 9 는 무조건 올림
        if last_num > 5:
            # 올린 횟수 덧셈
            answer += (10 - last_num)
            if len(l) > 0:
                # 올렸으니까 앞자리 수 1 더하기
                l[-1] += 1
            
        # 0, 1, 2, 3, 4 는 무조건 내림 
        elif last_num < 5:
            # 내린 횟수 덧셈
            answer += last_num
            
        # 5는
        else:
            # 앞자리 수가 5 이상이면 올리고
            if (len(l) > 0) and (l[-1] >= 5):
                answer += (10 - last_num)
                l[-1] += 1
            # 아니면 내림
            else:
                answer += 5
    # 맨 앞자리를 올렸다면 1이 됐을 것이고 아니면 0
    answer += l[0]
    return answer


# 5555 5
# 5560 4
# 5600 4
# 6000 4
# 10000 1