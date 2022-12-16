def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        # 도시 이름 소문자로 통일
        city = city.lower()
        
        # 캐시 사이즈가 일정 수준보다 크다면 오래된 원소 제거
        if len(cache) > cacheSize:
            cache.pop(0)
        
        # 만약 hit 라면
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        
        # 만약 miss라면
        else:
            cache.append(city)
            answer += 5
    return answer


################################################
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    l = [''] * 3

    # 길이를 체크할 필요가 없음
    cache = deque(l, maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        # hit
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        # miss
        else:
            cache.append(city)
            answer += 5
    return answer