def solution(n):
    a = str(n)
    sum_digit = 0
    for i in range(len(a)):
        sum_digit += int(a[i])
    return sum_digit

def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)
