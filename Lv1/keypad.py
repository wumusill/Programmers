def solution(numbers, hand):
    result = []
    left_hand = 10
    right_hand = 12
    dist_left = 0
    dist_right = 0

    for i in numbers:
        if i == 0:
            i = 11

        if i in [1, 4, 7]:
            result.append("L")
            left_hand = i
        elif i in [3, 6, 9]:
            result.append("R")
            right_hand = i
        else:
            dist_left = abs(i - left_hand)
            dist_right = abs(i - right_hand)


            if sum(divmod(dist_left, 3)) > sum(divmod(dist_right, 3)):
                result.append('R')
                right_hand = i
            elif sum(divmod(dist_left, 3)) < sum(divmod(dist_right, 3)):
                result.append('L')
                left_hand = i
            else:
                if hand == 'right':
                    result.append('R')
                    right_hand = i
                else:
                    result.append('L')
                    left_hand = i

    return "".join(result)

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))