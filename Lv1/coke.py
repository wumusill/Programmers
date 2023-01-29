def solution(a, b, n):
    answer = 0
    mod = 0
    while n >= a:
        answer += n // a * b
        mod = n % a
        n = n // a * b + mod
    
    return answer