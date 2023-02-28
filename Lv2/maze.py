# 생각하지 않았던 애먹었던 경우
# "O" 뿐만 아니라 "E", "S"도 지나갈 수 있는 길이다.
# "L"을 들리지 않고 "E"를 지나가면 방문 처리가 된다. -> 마지막 이중 for문에서 문제 발생
from collections import deque

def solution(maps):
    answer = 0
    q = deque()
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    lever = False
    
    # 출발지에서 레버까지 bfs
    maps = [list(i) for i in maps]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # 출발지에서 시작
            if maps[i][j] == "S":
                visited[i][j] == 0
                q.append((0, i, j))
                while q:
                    t, x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                            continue
                        if maps[nx][ny] == "O" and visited[nx][ny] == -1:
                            visited[nx][ny] = 0
                            q.append((t+1, nx, ny))
                        if maps[nx][ny] == "E" and visited[nx][ny] == -1:
                            visited[nx][ny] = 0
                            q.append((t+1, nx, ny))
                        if maps[nx][ny] == "L" and visited[nx][ny] == -1:
                            answer += (t + 1)
                            lever = True
                            q.clear()
                            break
                # 레버 작동했으면 for문 탈출
                if lever:
                    break
            # 레버 작동했으면 for문 탈출
            if lever:
                break
   
    # 레버를 작동했을 때만 실행되는 반복문
    # 레버에서 EXIT까지 bfs
    if lever: 
        # 큐와 방문 기록 초기화
        q = deque()
        Exit = False
        visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                # 레버에서 출발
                if maps[i][j] == "L":
                    visited[i][j] == 0
                    q.append((0, i, j))
                    while q:
                        t, x, y = q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                                continue
                            if maps[nx][ny] == "O" and visited[nx][ny] == -1:
                                visited[nx][ny] = 0
                                q.append((t+1, nx, ny))
                            if maps[nx][ny] == "S" and visited[nx][ny] == -1:
                                visited[nx][ny] = 0
                                q.append((t+1, nx, ny))
                            # START부터 Lever까지의 거리 + Lever에서 EXIT까지의 거리
                            # EXIT 방문 처리
                            if maps[nx][ny] == "E":
                                answer += (t + 1)
                                visited[nx][ny] = 0
                                q.clear()
                                Exit = True
                                break
                if Exit:
                    break
            if Exit:
                break
                            

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            # EXIT에 방문 기록이 있으면 거리 출력
            # 기록이 없으면 방문 불가 -1 출력
            if maps[i][j] == "E":
                if visited[i][j] == -1 or not lever:
                    return -1
                else:
                    return answer