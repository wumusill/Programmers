############################## 시간초과 ##############################
# 완전탐색?
# 앞뒤 똑같은 알파벳이 있으면 제거
def solution(s):
    length = len(s)
    alphabets = set(list(s))
    while True:
        for alpha in alphabets:
            s = s.replace(alpha * 2, "")
            if len(s) == 0:
                return 1
        if len(s) == length:
            return 0
####################################################################
# stack을 활용
def solution(s):
    l = list(s)
    stack = []
    for i in l:
        if not stack:
            stack.append(i)
            continue
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1


print(solution("baabaa"))
print(solution("cdcd"))