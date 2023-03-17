def solution(keymap, targets):
    answer = []
    # 최솟값을 저장할 사전
    cnt = {}
    
    # 키보드의 자판들을 순회
    for word in keymap:
        for idx, letter in enumerate(word):
            # 만약 처음 등장한 알파벳이라면 저장
            if letter not in cnt:
                cnt[letter] = idx + 1
            # 이미 등장한 알파벳이라면 최솟값 비교 후 저장
            else:
                cnt[letter] = min(cnt[letter], idx+1)
    
    # target 순회 
    for target in targets:
        # 자판 눌러야 하는 횟수
        res = 0
        for spell in target:
            # 만약 최솟값이 없는 알파벳이라면 == 만들 수 없는 단어
            if spell not in cnt:
                answer.append(-1)
                # 반복문이 중단되었음을 알리기 위해 0으로 초기화
                res = 0
                break
            # 최솟값의 합 기록
            res += cnt[spell]
            
        # 반복문이 중단 없이 다 순회했을 경우 res 기록
        if res > 0:
            answer.append(res)
            
    return answer