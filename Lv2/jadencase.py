def solution(s):
    l = list(s)
    ans_l = []
    ans_l.append(l[0].upper())
    for i in range(1, len(l)):
        if l[i-1].isspace() == True and l[i].isspace() == False:
            ans_l.append(l[i].upper())
        else:
            ans_l.append(l[i].lower())
    return ''.join(ans_l)


print(solution('3people unFollowed me'))
print(solution('for the last week'))
print(solution('i am a     man'))