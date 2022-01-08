def solution(arr):
    l = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            continue
        else:
            l.append(arr[i])
    return l


print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3])


def no_continuous(s):
    result = []
    for c in s:
        if (len(result) == 0) or (result[-1] != c):
            result.append(c)
    return result


def no_continuous_2(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a