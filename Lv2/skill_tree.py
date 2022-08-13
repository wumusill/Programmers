from collections import deque


def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        order = deque(list(skill))
        s = list(s)
        flag = True
        for spell in s:
            if spell not in order:
                continue
            else:
                if spell != order[0]:
                    flag = False
                    break
                else:
                    order.popleft()
        if flag:
            answer += 1

    return answer