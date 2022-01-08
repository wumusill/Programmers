def solution(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2 -1:length//2+1]
    else:
        return s[length//2]



def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]