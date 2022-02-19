def solution(s):
    l = list(s)
    answer = [0, 0]
    while True:
        if len(l) == 1:
            break

        answer[1] += l.count('0')
        l = bin(l.count('1'))[2:]
        answer[0] += 1

    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))