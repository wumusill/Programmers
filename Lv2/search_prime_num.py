from itertools import permutations


def solution(numbers):
    answer = []
    l = list(numbers)
    for k in range(1, len(l) + 1):
        all_case = list(permutations(l, k))

        for case in all_case:
            is_prime = True
            num = int(''.join(case))
            if num == 1:
                continue

            if num == 2 and 2 not in answer:
                answer.append(2)

            if num % 2 == 1:
                for j in range(3, int(num ** 0.5) + 1, 2):
                    if num % j == 0:
                        is_prime = False
                if is_prime == True and num not in answer:
                    answer.append(num)

    return len(answer)


print(solution("17"))
print(solution("011"))
print(solution('9'))
print(solution('20'))