from itertools import product


def solution(word):
    ans_list = []
    aeiou = ["A", "E", "I", "O", "U"]

    for i in range(1, 6):
        ans_list.extend(list(product(aeiou, repeat=i)))

    ans_list.sort()
    ans = tuple(word)

    return ans_list.index(ans) + 1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))