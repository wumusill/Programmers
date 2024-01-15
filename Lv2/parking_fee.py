# 주차 시간을 분으로 환산
def calculate_time(time_in, time_out):
    # 입차, 출차 시간 시와 분 분리
    time_in_h, time_in_m = time_in.split(':')
    time_out_h, time_out_m = time_out.split(':')

    # 시와 분을 분으로 환산하고 둘의 차를 반환
    min_in = int(time_in_h) * 60 + int(time_in_m)
    min_out = int(time_out_h) * 60 + int(time_out_m)

    return min_out - min_in


def solution(fees, records):
    parking = {}
    parking_time = {}
    for record in records:
        time, num, status = record.split()
        if status == 'IN':                                                  # 입차 시간 기록
            parking[num] = time
        elif status == 'OUT':                                               # 출차 시간
            if num in parking_time:                                         # 이미 입출차한 기록이 있으면 시간 계산 후 합산
                parking_time[num] += calculate_time(parking[num], time)
            else:
                parking_time[num] = calculate_time(parking[num], time)      # 첫 출차면 주차 시간 기록
            del parking[num]                                                # 차량 번호 제거

    if parking:                                                             # 남아 있는 차량은 23:59 출차 처리
        for num in parking:
            if num in parking_time:
                parking_time[num] += calculate_time(parking[num], "23:59")
            else:
                parking_time[num] = calculate_time(parking[num], "23:59")

    fee = {}
    for num, time in parking_time.items():
        if time > fees[0]:                                                  # 요금 계산
            fee[int(num)] = fees[1] + (time - fees[0]) // fees[2] * fees[3]
            if (time - fees[0]) % fees[2] > 0:
                fee[int(num)] += fees[3]
        else:                                                               # 기본 요금
            fee[int(num)] = fees[1]

    answer = [val for key, val in sorted(fee.items(), key=lambda x: x[0])]  # 차량 번호 기준 주차 요금 오름차순 정렬

    return answer