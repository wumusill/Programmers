def solution(n):
    count_1_n = bin(n)[2:].count('1')
    answer = n + 1
    while True:
        count_1_a = bin(answer)[2:].count('1')
        if count_1_n == count_1_a:
            return answer
        answer += 1


print(solution(78))
print(solution(15))