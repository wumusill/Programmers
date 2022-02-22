def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in money:
        for j in range(i, n + 1):
            if j >= i:
                dp[j] += dp[j-i]

    return dp[n] % 1000000007


print(solution(5, [1, 2, 5]))
print(solution(6, [1, 2, 5]))

# https://programmers.co.kr/questions/25161

# 1: 1
# 2: (1, 1)    (2)
# 3: (1, 1, 1)     (2, 1)
# 4: (1, 1, 1, 1)         (1, 1, 2)    (2, 2)
# 5: (1, 1, 1, 1, 1)    (1, 1, 1, 2)   (1, 2, 2)        (5)
# 6: (1, 1, 1, 1, 1, 1)   (1, 1, 1, 1, 2)  (1, 1, 2, 2)  (2, 2, 2)  (5, 1)