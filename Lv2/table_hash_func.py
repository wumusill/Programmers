def solution(data, col, row_begin, row_end):
    mod_l = []

    # 조건에 맞게 정렬
    data.sort(key=lambda x: (x[col-1], -x[0]))
    
    for i in range(row_begin-1, row_end):
        mod = 0
        for j in data[i]:
            mod += j % (i+1)
        mod_l.append(mod)

    # XOR 연산자 == ^
    answer = 0
    for mod in mod_l:
        answer = answer ^ mod
    return answer 


print(solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8 ,3]], 2, 2, 3))

# [
#     [4, 2, 9],
#     [2, 2, 6],
#     [1, 5, 10],
#     [3, 8, 3]
# ]

# print(0 ^ 4)