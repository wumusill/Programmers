def solution(n):
    s = sorted(str(n), reverse=True)
    l = ''.join(s)
    return int(l)


print(solution(136152414))