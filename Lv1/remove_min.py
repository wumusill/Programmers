def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) != 0 else [-1]

print(solution([4, 3, 2, 1]))
print(solution([10]))


# 만약 최솟값이 여러개라면
def solution_2(arr):
    return [i for i in arr if i > min(arr)]