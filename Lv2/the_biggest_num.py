def solution(numbers):
    numbers = list(map(str, numbers))
    answer = []

    # 제한사항 중 하나로 numbers의 원소는 0 이상 1,000 이하
    # 최대 길이가 4
    # 정렬 기준은 숫자가 큰 순서대로
    # 하지만 숫자마다 길이가 달라 통일해줄 필요가 있음
    # 1, 2, 3, 4의 최소공배수인 12, 모든 숫자를 12자리로 만듦
    # 후에 합쳐야 하는 것은 원래 숫자이므로 임의로 만든 12자리 숫자와 함께 튜플로 저장 후 정렬
    for i in range(len(numbers)):
        numbers[i] = (numbers[i], numbers[i] * (12//len(numbers[i])))
    sorted_numbers = sorted(numbers, key=lambda x:x[1], reverse=True)

    # 정렬된 리스트에서 원래 숫자를 순서대로 리스트 만들고 합침
    for i in sorted_numbers:
        answer.append(i[0])

    # 만약 리스트에 0뿐이라면 합치지 않고 0을 리턴
    if len(answer) == answer.count('0'):
        return '0'
    return ''.join(answer)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

###########################################################
def solution_2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))