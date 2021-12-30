from itertools import combinations

def solution(nums):
    pick_3 = combinations(nums, 3)
    prime_num = 0
    for i in pick_3:
        sum_of_pick = sum(i)
        cnt = 0
        for j in range(3, sum_of_pick, 2):
            if sum_of_pick % j == 0:
                cnt += 1
                break
        if cnt == 0 and sum_of_pick % 2 != 0:
            prime_num += 1
    return prime_num


def prime_number(x):
    answer = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0

def solution_2(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums, 3)])