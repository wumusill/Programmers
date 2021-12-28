def solution(s):
    l = list(s)
    for i in range(len(l)):
        l[i] = ord(l[i])
    l = sorted(l, reverse=True)
    for i in range(len(l)):
        l[i] = chr(l[i])
    return ''.join(l)

def solution_2(s):
    return ''.join(sorted(s, reverse=True))