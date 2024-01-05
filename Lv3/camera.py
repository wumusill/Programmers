def solution(routes):
    answer = 1

    # 종료 구간 기준 오름차순 정렬
    routes.sort(key=lambda x: x[1])

    # 첫 번째 차량의 이동 구간, 종료 시점에 하나 설치, 최대한 끝에 설치해서 뒤 차량이 최대한 많이 걸칠 수 있도록 함
    before_a, before_b = routes[0][0], routes[0][1]

    # 두 번째 차부터 이동 구간 순회
    for a, b in routes[1:]:
        if a <= before_b <= b:          # 이전에 설치한 카메라를 지나는 차량이면 pass
            continue
        else:
            answer += 1                 # 이전에 설치한 카메라를 지나지 않으면 종료 시점에 하나 설치
            before_a, before_b = a, b   # 카메라 설치 구간 갱신

    return answer