def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        price = prices[i]
        cnt = 0
        for i in range(i, len(prices) - 1):
            if prices[i] >= price:
                cnt += 1
            else:
                break

        answer.append(cnt)
    answer.append(0)
    return answer