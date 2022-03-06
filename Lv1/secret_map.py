def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:].zfill(n)
        arr2[i] = bin(arr2[i])[2:].zfill(n)
    for str1, str2 in zip(arr1, arr2):
        string = ''
        for spell1, spell2 in zip(str1, str2):
            if spell1 == '1' or spell2 == '1':
                string += '#'
            else:
                string += ' '

        answer.append(string)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))