def solution(absolutes, signs):
    answer = 0
    for x, y in zip(absolutes, signs):
        if y == True:
            answer += x
        else:
            answer -= x
    return answer

print(solution([4, 7, 12], [True, False, True]))