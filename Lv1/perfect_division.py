def solution(arr, divisor):
    l = []
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            l.append(i)
    return l if len(l) != 0 else [-1]


def solution_2(arr, divisor): return sorted([n for n in arr if n % divisor == 0]) or [-1]
# 리스트는 값이 있으면 True, 값이 없는 빈 리스트는 False를 return 한다
# or 앞이 참이라면 해당 값까지만, 거짓일 경우 뒤의 것을 호출


def solution_3(arr, divisor):
    arr = [x for x in arr if x % divisor ==0]
    arr.sort()
    return arr if len(arr) != 0 else [-1]