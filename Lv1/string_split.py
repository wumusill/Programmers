def solution(s):
    answer = 0
    first_letter = ""
    first_cnt = 0
    other_cnt = 0
    
    # 문자열 순회
    for letter in s:
        # 첫 문자열
        if first_letter == "":
            first_letter = letter
            first_cnt += 1
        else:
            # 첫 문자 개수 갱신
            if first_letter == letter:
                first_cnt += 1
            # 첫 문자와 다른 문자의 개수 갱신
            else:
                other_cnt += 1
        # 두 개수가 같아지면 문자열 분리하고 기록 모두 초기화
        if first_cnt == other_cnt:
            first_letter = ""
            first_cnt = 0
            other_cnt = 0
            answer += 1

    # 문자열을 다 순회했는데 기록이 초기화 되어있지 않다면 = om-eg-a와 같은 케이스, 마지막 알파벳 분리
    if first_letter != "":
        answer += 1
    return answer