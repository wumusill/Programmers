# 영어 끝말잇기

def solution(n, words):
    answer = [0, 0]

    for i in range(1, len(words)):
        last_spell = words[i - 1][-1]
        first_spell = words[i][0]

        if words[i] in words[:i]:
            answer[0] += i % n + 1
            answer[1] += i // n + 1
            return answer

        if last_spell != first_spell:
            answer[0] += i % n + 1
            answer[1] += i // n + 1
            return answer

    return answer