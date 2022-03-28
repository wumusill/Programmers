# k진수에서 소수 개수 구하기
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    reverted_num = ''
    mod_list = '012'
    answer = 0
    for i in range(3, k):
        mod_list += str(i)

    while n > 0:
        reverted_num += mod_list[n % k]
        n //= k

    reverted_num = reverted_num[::-1].split('0')

    for i in reverted_num:
        if i == '':
            continue
        if isprime(int(i)) == True:
            answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))