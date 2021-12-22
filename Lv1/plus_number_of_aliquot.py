def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        sqrt_of_i = i ** (1/2)
        question = sqrt_of_i % 1
        if question == 0 :
            answer -= i
        else:
            answer += i
    return answer