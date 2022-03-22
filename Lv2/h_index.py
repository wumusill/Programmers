def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    return len(citations)


def solution_2(citations):
    citations.sort(reverse = True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

print(solution([3, 0, 6, 1, 5]))  # 3
print(solution([4, 4, 4]))  # 3
print(solution([1, 2, 3, 4, 5, 6]))  # 3

print(solution_2([3, 0, 6, 1, 6]))
print(solution_2([4, 4, 4]))
print(solution_2([1, 2, 3, 4, 5, 6]))