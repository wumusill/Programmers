from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque()
    rest = [100 - progresses[i] for i in range(len(progresses))]
    needed_days = [rest[i] // speeds[i] if rest[i] % speeds[i] == 0 else (rest[i] // speeds[i]) + 1 for i in range(len(progresses))]

    for i in range(len(progresses)):
        if not queue:
            queue.append(needed_days[i])
        else:
            if queue[0] >= needed_days[i]:
                queue.append(needed_days[i])
            else:
                answer.append(len(queue))
                queue.clear()
                queue.append(needed_days[i])

    answer.append(len(queue))

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(solution([96, 94], [3, 3]))
print(solution([99, 1, 99, 1], [1, 1, 1, 1])) # [1, 3]