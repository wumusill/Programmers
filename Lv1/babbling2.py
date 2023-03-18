def solution(babbling):
    answer = 0
    # 말할 수 있는 단어들
    cans = ["aya", "ye", "woo", "ma"]
    
    # 말할 수 없는 연속 단어들
    cants = ["ayaaya", "yeye", "woowoo", "mama"]

    # index와 단어 순회
    for idx, word in enumerate(babbling):
        # 말할 수 없는 단어 치환
        for cant in cants:
            word = word.replace(cant, "X")
        # 말할 수 있는 단어 치환
        for can in cans:
            word = word.replace(can, "O")
        
        # 해당 index에 치환된 단어 저장
        babbling[idx] = word

    # 단어 순회
    for word in babbling:
        # 철자 분리 -> 중복 제거 -> index 활용 위해 다시 list
        temp = list(set(list(word)))
        # 말할 수 있는 단어라면 "O"만 남아있는 상황
        if len(temp) == 1 and temp[0] == "O":
            answer += 1
    return answer