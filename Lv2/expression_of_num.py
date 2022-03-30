def solution(n):
    answer = 0
    l = [1]
    for i in range(2, 141):
        l.append(l[-1] + i)
    if n in l:
        answer += 1

    for _ in range(10000):
        for j in range(len(l)):
            l[j] += j + 1
            if l[j] >= 10000:
                break
        if n in l:
            answer += 1

    return answer


print(solution(15))


# (1부터) 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
# (2부터) 2, 5, 9, 14, 20, 27, 35, 44, 54
# (3부터) 3, 7, 12, 18, 25, 33, 42, 52
# (4부터) 4, 9, 15, 22, 30, 39, 49, 60

def solution_2(num):
    return len([i for i in range(1, num + 1, 2) if num % i == 0])

print(solution_2(15))