def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1


def sumMatrix(A, B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
    return answer

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))

print(sumMatrix([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(sumMatrix([[1], [2]], [[3], [4]]))