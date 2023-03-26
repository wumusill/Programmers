def solution(park, routes):
    # S, 출발지를 찾기 위한 반복문
    breaker = False
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x = i
                y = j
                breaker = True
                break
        if breaker:
            break
    
    # 입력된 명령 순회
    for route in routes:
        # 방향과 거리 분리
        direct, cnt = route.split()
        cnt = int(cnt)
        # 방향이 북쪽이라면 거리만큼 위로 이동
        # elif 로 각각 남, 서, 동 방향 동일한 로직
        if direct == "N":
            # 거리만큼 순회
            for i in range(1, cnt+1):
                nx = x - i
                ny = y
                # 공원 범위를 벗어난다면 명령 무시
                if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                    break
                # 가는 도중 벽을 만난다면 명령 무시
                if park[nx][ny] == "X":
                    break
            # 반복문을 다 돌았다면 == 범위도 벗어나지 않고 벽도 만나지 않는, 정상적인 명령이었다면
            # x, y 업데이트
            else:
                x = nx
                y = ny
        elif direct == "S":
            for i in range(1, cnt+1):
                nx = x + i
                ny = y
                if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                    break
                if park[nx][ny] == "X":
                    break
            else:
                x = nx
                y = ny
        elif direct == "W":
            for i in range(1, cnt+1):
                nx = x
                ny = y - i
                if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                    break
                if park[nx][ny] == "X":
                    break
            else:
                x = nx
                y = ny
        elif direct == "E":
            for i in range(1, cnt+1):
                nx = x
                ny = y + i
                if nx < 0 or ny < 0 or nx >= len(park) or ny >= len(park[0]):
                    break
                if park[nx][ny] == "X":
                    break
            else:
                x = nx
                y = ny
                
    return [x, y]