# 첫 풀이, 89.5점
def solution(book_time):
    answer = 0
    # 시작 시간을 기준으로 시간 오름차순 정렬
    book_time.sort()
    
    # 각 방의 예약 시간표, 최대 예약 개수만큼 방이 필요하기 때문에 방의 개수만큼 mat 생성
    table = [[] for _ in range(len(book_time))]

    # 예약 시간 순회
    for start, end in book_time:
        # 각 방 예약 시간표 순회
        for i in range(len(table)):
            # 만약 방이 비어있다면 예약
            if not table[i]:
                table[i].append([start, end])
                answer += 1
                # 예약이 됐다면 바로 다음 방을 확인하기 위해 for문 break
                break
            
            # 방이 비어있지 않다면 마지막 예약 시간의 퇴실 시간 저장
            pre_h, pre_m = map(int, table[i][-1][1].split(':'))
            # 지금 순회 중인 시간의 입실 시간 저장
            now_h, now_m = map(int, start.split(':'))
            
            # 10분의 청소시간이 필요하기 때문에
            # (퇴실 시간+10분)이 입실 시간보다 작거나 같다면 예약
            if (pre_h + 1 <= now_h and pre_m - 60 <= now_m) or (pre_h == now_h and pre_m + 10 <= now_m):
                table[i].append([start, end])
                break
                
    return answer 
##########################################################################################################
# 정답 풀이
# 가장 큰 차이점 : 시간을 분으로 통일
# 로직은 위와 같음 다만 시간 비교할 때 시와 분을 따로 비교하지 않고 분으로 통일하여 비교
def solution(book_time):
    answer = 0
    minute = []
    
    # 모든 입실 시간과 퇴실 시간을 순회
    for start, end in book_time:
        # 입실 시간을 시와 분으로 분리
        s_h, s_m = map(int, start.split(":"))
        # 퇴실 시간을 시와 분으로 분리
        e_h, e_m = map(int, end.split(":"))
        # 입실 시 * 60 + 입실 분
        start = s_h * 60 + s_m
        # 퇴실 시 * 60 + 퇴실 분
        end = e_h * 60 + e_m

        # 분으로 통일 후 저장
        minute.append((start, end))
    
    # 시간(분) 오름차순 정렬
    minute.sort()
    
    # 각 방의 예약 시간표, 최대 예약 개수만큼 방이 필요하기 때문에 방의 개수만큼 mat 생성
    table = [[] for _ in range(len(book_time))]

    # 예약 시간 순회
    for start, end in minute:
        # 각 방 예약 시간표 순회
        for i in range(len(table)):
            # 만약 방이 비어있다면 예약
            if not table[i]:
                table[i].append([start, end])
                answer += 1
                # 예약이 됐다면 바로 다음 방을 확인하기 위해 for문 break
                break
            
            # 방이 비어있지 않다면 마지막 예약 시간의 입/퇴실 시간 저장
            pre_start, pre_end = table[i][-1]
            
            # 퇴실 시간 + 10분이 순회 중인 입실 시간보다 작거나 같다면 예약
            if pre_end + 10 <= start:
                table[i].append([start, end])
                break
        
    return answer 