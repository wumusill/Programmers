def solution(s, skip, index):
    # ord("a"), ord("z") : 97, 122
    answer = ""
    s = list(map(ord, list(s)))
    skip_list = list(map(ord, list(skip)))
    
    for code in s:
        t = 0
        while t < index:
            code += 1
            if code == 123:
                code = 97
            if code not in skip_list:
                t += 1
        answer += chr(code)
    return answer