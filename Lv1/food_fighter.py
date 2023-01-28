def solution(food):
    answer = '0'
    for i in range(len(food) - 1, 0, -1):
        times = food[i] // 2
        answer = str(i) * times + answer + str(i) * times
    return answer