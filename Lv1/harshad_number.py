def solution(x):
    sum_of_digits = sum(map(int, list(str(x))))
    if x % sum_of_digits == 0:
        return True
    else:
        return False


def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0