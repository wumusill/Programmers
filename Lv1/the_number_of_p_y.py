def solution(s):
    s_list = list(s.lower())
    num_p = 0
    num_y = 0
    for i in s_list:
        if i == 'p':
            num_p += 1
        elif i == 'y':
            num_y += 1
    return True if num_p == num_y else False

def solution_2(s):
    return s.lower().count('p') == s.lower().count('y')