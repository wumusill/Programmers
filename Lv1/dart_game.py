def solution(dartResult):
    score = []
    idx = 0
    for i in range(len(dartResult)):
        if dartResult[i] in ('S', 'D', 'T'):
            num = int(dartResult[idx:i])
            if dartResult[i] == 'D':
                num = num ** 2
            elif dartResult[i] == 'T':
                num = num ** 3
            score.append(num)
            if i + 1 < len(dartResult) and dartResult[i + 1] in ('#', '*'):
                idx = i + 2
            else:
                idx = i + 1
        if dartResult[i] in ('#', '*'):
            if dartResult[i] == '*':
                if len(score) > 1:
                    score[-1] *= 2
                    score[-2] *= 2
                else:
                    score[-1] *= 2
            else:
                score[-1] *= -1

    return sum(score)


print(solution('1S2D*3T'))  # 37
print(solution('1D2S#10S'))  # 9
print(solution('1D2S0T'))  # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D#2S*3S')) # 5
print(solution('1T2D3D#'))  # -4
print(solution('1D2S3T*'))  # 59

################################################################################################

def solution(s):
    점수 = []
    for num, i in enumerate(s):
        if i == 'S':
            점수[-1] **= 1
        elif i == 'D':
            점수[-1] **= 2
        elif i == 'T':
            점수[-1] **= 3
        elif i == '*':
            점수[-1] *= 2
            if len(점수) >= 2:
                점수[-2] *= 2
        elif i == '#':
            점수[-1] *= -1
        else:
            if s[num:num+2] == '10':
                점수.append(10)
            elif s[num-1:num+1] != '10':
                점수.append(int(i))
    return sum(점수)

################################################################################################
# 정규 표현식 이용한 풀이
import re

def solution(dartResult):
    패턴 = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    answer = []
    계산식 = {
        'S':lambda 값:값, 
        'D':lambda 값:값**2, 
        'T':lambda 값:값**3
    }
    for 숫자, 승수, 상 in 패턴.findall(dartResult):
        print(숫자, 승수, 상)
        if 승수 == 'S':
            점수 = 계산식['S'](int(숫자))
        elif 승수 == 'D':
            점수 = 계산식['D'](int(숫자))
        elif 승수 == 'T':
            점수 = 계산식['T'](int(숫자))
        if 상 == '*':
            점수 *= 2
            if answer:
                answer[-1] *= 2
        elif 상 == '#':
            점수 *= -1
        answer.append(점수)
        
    return sum(answer)
            
print(solution('1S2D*3T'))