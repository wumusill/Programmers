from collections import deque

# 시간 초과 : sum 함수 활용
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    while truck_weights:
        time += 1
        bridge.popleft()
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)

        else:
            bridge.append(0)
    time += bridge_length
    return time
######################################################################################
# 통과 : sum 함수 미활용, 큰 차이를 보임
def solution(bridge_length, weight, truck_weights):
    time, w = 0, 0
    bridge = deque([0] * bridge_length)
    while truck_weights:
        time += 1

        # 1초가 지날 때마다 무조건 빠져나갈 수 있도록 미리 다리에서 제거
        w -= bridge.popleft()

        # 만약 남은 차가 있고 다리에 올라갈 수 있으면 올라가고 무게 갱신
        if truck_weights and w + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            w += truck
        else:
            bridge.append(0)

    # 더 건날 차가 없으면 다리 길이만큼 시간 추가
    time += bridge_length

    return time