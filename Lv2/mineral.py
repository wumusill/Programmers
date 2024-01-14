def solution(picks, minerals):
    # 캘 수 있는 광물의 수 = (곡괭이 * 5), 광물의 개수가 이보다 적으면 다 캘 수 있음
    can = min(sum(picks) * 5, len(minerals))

    all_minerals = []
    for i in range(0, can, 5):                                  # 캘 수 있는 광물
        splited_minerals = minerals[i:i + 5]                    # 5개씩 분리
        cnt_minerals = {'diamond': 0, 'iron': 0, 'stone': 0}
        for mineral in splited_minerals:                        # 분리된 5개 광물에서
            cnt_minerals[mineral] += 1                          # 각 광물에 대한 개수 갱신
        all_minerals.append(cnt_minerals)                       # 기록된 개수 저장

    # 캘 수 있는 광물을 (다이아몬드, 철, 돌) 기준 내림차순 정렬
    all_minerals.sort(key=lambda x: (-x['diamond'], -x['iron'], -x['stone']))

    # 각 곡괭이로 광물을 캘 때 소모되는 피로도
    diamond_pick = {'diamond': 1, 'iron': 1, 'stone': 1}
    iron_pick = {'diamond': 5, 'iron': 1, 'stone': 1}
    stone_pick = {'diamond': 25, 'iron': 5, 'stone': 1}

    # 곡괭이 개수 {곡괭이 : 개수} 로 변경
    picks = {pick: cnt for pick, cnt in zip(['diamond', 'iron', 'stone'], picks)}
    answer = 0
    while all_minerals:                                     # 캘 수 있는 모든 광물 다 캘 때까지
        minerals = all_minerals.pop(0)                      # 첫 광물
        if picks['diamond'] > 0:                            # 다이아몬드 곡괭이 있으면
            picks['diamond'] -= 1                           # 하나 소비
            for mineral, cnt in minerals.items():
                answer += diamond_pick[mineral] * cnt       # 소모된 피로도 기록
        elif picks['iron'] > 0:
            picks['iron'] -= 1
            for mineral, cnt in minerals.items():
                answer += iron_pick[mineral] * cnt
        elif picks['stone'] > 0:
            picks['stone'] -= 1
            for mineral, cnt in minerals.items():
                answer += stone_pick[mineral] * cnt

    return answer