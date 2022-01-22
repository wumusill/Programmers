def solution(n):
    remainder = []
    while n >= 1:
        remainder.append(n % 3)
        n //= 3

    nums = list(reversed(remainder))
    answer = 0

    for i in range(len(nums)):
        answer += (3 ** (i)) * nums[i]

    return answer

print(solution(45))
print(solution(125))

########################################################################
def solution_2(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer