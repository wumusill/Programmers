# 정답 코드
def solution(n, m, section):
    answer = 0
    while section:
        s = section.pop(0)
        while section and s + m > section[0]:
            section.pop(0)
        answer += 1
    return answer 

# 첫 시도 코드
def solution(n, m, section):
    answer = 0
    mi, ma = section[0], section[-1]
    
    for i in range(mi, ma+1, m):
        while section and i > section[0]:
            section.pop(0)
        answer += 1
    return answer 