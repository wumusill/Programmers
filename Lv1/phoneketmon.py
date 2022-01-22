def solution(nums):
    answer = len(set(nums))
    chance = len(nums) // 2
    return answer if answer <= chance else chance

#########################################################################
def solution_2(ls):
    return min(len(ls)/2, len(set(ls)))
