# 시간 초과
def solution(X, Y):
    l_x = list(X)
    set_x = list(X)
    set_y = list(Y)
    set_inter = []
    for i in l_x:
        if i in set_y:
            set_inter.append(i)
            set_x.remove(i)
            set_y.remove(i)
    
    if not set_inter:
        return "-1"
    
    return str(int(''.join(sorted(set_inter, reverse=True))))
#############################################################################
# remove가 비효율적이라고 생각해
# pop, append를 이용해 구현해봤으나 역시나 시간 초과
def solution(X, Y):
    l_x = sorted(list(X))
    l_y = sorted(list(Y))
    set_inter = []
    idx_x = 0
    idx_y = 0

    while True:
        if idx_x >= len(l_x) or idx_y >= len(l_y):
            break
        if len(l_x) == 0 or len(l_y) == 0:
            break
        if l_x[idx_x] == l_y[idx_y]:
            res = l_x.pop(idx_x)
            l_y.pop(idx_y)
            set_inter.append(res)
        elif l_x[idx_x] > l_y[idx_y]:
            idx_y += 1
        elif l_x[idx_x] < l_y[idx_y]:
            idx_x += 1

    if not set_inter:
        return "-1"

    return str(int(''.join(sorted(set_inter, reverse=True))))
#############################################################################
# 0~9까지 돌면서 숫자들의 개수를 활용하는 방법
# 시간 초과
def solution(X, Y):
    answer = ''
    for i in range(9, -1, -1):
        num = str(i)
        answer += num * min(X.count(num), Y.count(num))
    if answer == "":
        return "-1"
    return str(int(answer))
#############################################################################
# count가 비효율적인가 사전을 활용하여 개수를 연산해도
# 시간 초과
# 마지막 return 에서 형변환 시 많은 시간 소요 -> "0000"이 출력되는 것 방지하기 위함
def solution(X, Y):
    answer = ''
    
    dict_x = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    dict_y = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    
    for x in X:
        dict_x[x] += 1
    for y in Y:
        dict_y[y] += 1
    
    for i in range(9, -1, -1):
        num = str(i)
        answer += num * min(dict_x[num], dict_y[num])
    
    if answer == "":
        return "-1"

    return str(int(answer))
#############################################################################
# 형변환을 하지 않고 조건문을 통해 "0000"이 출력되는 것 방지
def solution(X, Y):
    answer = ''
    
    dict_x = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    dict_y = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    
    for x in X:
        dict_x[x] += 1
    for y in Y:
        dict_y[y] += 1
    
    for i in range(9, -1, -1):
        num = str(i)
        if num == '0' and answer == "" and dict_x["0"] != 0 and dict_y["0"] != 0:
            return "0"                        
        else:
            answer += num * min(dict_x[num], dict_y[num])
    
    if answer == "":
        return "-1"

    return answer