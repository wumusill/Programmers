# 숫자들을 처음부터 차례로 stack에 넣는데 stack의 가장 위에 있는 수가 넣으려고 하는 수보다 크면 그냥 넣고,
# 작으면 큰 값이 나올 때까지 stack에 있는 값들을 pop을 해준 뒤 stack에 넣어준다.
# pop할 때마다 k를 감소시켜주고, k가 0이 되면 더 이상 삭제할 수 없으므로 남은 수를 모두 넣어준다.
# 수를 끝까지 다 비교했는데 아직 삭제해야 할 수인 k가 남아있으면 k의 값만큼 뒤에서부터 잘라준다.
# 이렇게 풀 수 있는 이유는 가장 큰 수는 앞자리 수가 크면 되기 때문에 뒤는 잘라도 상관없다.

def solution(number, k):
    stack = [number[0]]
    idx = 1

    while idx < len(number):
        if not stack:
            stack.append(number[idx])
            idx += 1
        if k == 0:
            num = ''.join(stack)
            return num + number[idx:]

        if stack[-1] < number[idx]:
            stack.pop()
            k -= 1
        else:
            stack.append(number[idx])
            idx += 1

    if k > 0:
        num = ''.join(stack)
        return num[:len(num) - k]

    return ''.join(stack)


print(solution("1924", 2))
print(solution("1294", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)