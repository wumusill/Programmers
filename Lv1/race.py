def solution(players, callings):
    
    name_key = {name:idx for idx, name in enumerate(players)}
    rank_key = {idx:name for idx, name in enumerate(players)}
    
    # 호명된 선수 순회
    for name in callings:
        # 호명된 선수 순위 파악
        rank = name_key[name]

        # 호명된 선수 앞 선수 이름 저장 
        pre_person = rank_key[rank - 1]

        # 호명된 선수와 앞 선수 순위 변경 
        rank_key[rank], rank_key[rank - 1] = rank_key[rank - 1], rank_key[rank]
        name_key[pre_person], name_key[name] = name_key[name], name_key[pre_person]
        
    return list(rank_key.values())

# ['mumu', 'kai', 'mine', 'soe', 'poe']
print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))