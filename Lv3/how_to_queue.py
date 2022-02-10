from math import factorial

def solution(n, k):
    answer = []
    l = [i for i in range(1, n+1)]

    for i in range(n-1, -1, -1):
        index = k // factorial(i)
        remainder = k % factorial(i)

        # 나머지가 있으면 몫을 인덱스로하고 나머지를 다시 나누기
        if remainder != 0:
            answer.append(l[index])
            del l[index]
            k = remainder
        # 나누어 떨어지면 몫-1 을 인덱스로하고 나머지의 revesed_list 를 뒤에 더하기
        else:
            answer.append(l[index-1])
            del l[index-1]
            l.reverse()
            return answer + l

print(solution(3, 5))
print(solution(5, 10))
print(solution(5, 50))