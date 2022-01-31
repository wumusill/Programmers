def solution(s):
    l = list(s)
    ans = 0

    for i in l:
        if i == '(':
            ans += 1
        elif i == ')':
            ans -= 1
        if ans < 0:
            return False

    if ans == 0:
        return True
    else:
        return False