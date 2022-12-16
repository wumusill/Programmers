def solution(s):
    # 정답 리스트
    answer = []
    # 알파벳 사전, 등장한 알파벳 기록
    spell_dict = {}

    # 알파벳 하나씩 순회
    for alphabet in list(s):
        # 만약 처음 등장한 알파벳이라면
        if alphabet not in spell_dict.keys():
            # 사전에 기록하고
            spell_dict[alphabet] = 1
            # 처음 등장했으므로 answer에 -1 추가
            answer.append(-1)
        # 처음 등장한 알파벳이 아니라면
        else:
            # (사전에 기록된 값 - 1)을 answer 에 추가
            res = spell_dict[alphabet] - 1
            answer.append(res)
            spell_dict[alphabet] = 1
        
        # 사전에 기록된 모든 알파벳 += 1
        for key in spell_dict.keys():
            spell_dict[key] += 1
    return answer