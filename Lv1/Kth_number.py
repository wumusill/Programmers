def solution(array, commands):
    answer = []
    for command_array in commands:
        i = command_array[0]
        j = command_array[1]
        k = command_array[2]
        new_array = array[i-1:j]
        sorted_array = sorted(new_array)
        answer.append(sorted_array[k-1])
    return answer

# def solution(array, commands):
#     return list(map(lambda x: sorted(array[x[0]-1:x[1]])[[x[2]-1]], commands))

# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i, j ,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer