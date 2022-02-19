def solution(clothes):
    answer = 1
    dict = {}
    for clothes, type in clothes:
        if type in dict.keys():
            dict[type] += 1
        else:
            dict[type] = 1

    # 소인수분해 후 약수의 개수 구하는 것과 동일
    # 해당 type 안입는 경우 + 1 곱해주는 것
    for j in dict.values():
        answer *= (j+1)

    # 아무것도 입지 않는 경우 제거
    return answer - 1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

# 곱하고 1 빼면 되는 이유 :
# ex : (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc