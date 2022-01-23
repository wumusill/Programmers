def solution(s):
    l = list(map(int, s.split()))
    answer_list = []

    answer_list.append(min(l))
    answer_list.append(max(l))

    answer = list(map(str, answer_list))
    answer = ' '.join(answer)
    return answer

########################################################################
def solution_2(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))