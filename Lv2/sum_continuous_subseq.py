# list로 구현
def solution(elements):
    length = len(elements)
    temp = list(set(elements))
    elements *= 2

    for i in range(2, length + 1):
        for j in range(length):
            _sum = sum(elements[j:j + i])
            temp.append(_sum)
    
    return len(set(temp))


############################################################
# set으로 구현, 더 나은 속도를 보임
def solution(elements):
    length = len(elements)
    temp = set(elements)
    elements *= 2

    for i in range(2, length + 1):
        for j in range(length):
            _sum = sum(elements[j:j + i])
            temp.add(_sum)
    
    return len(temp)