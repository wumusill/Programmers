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