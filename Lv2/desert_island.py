# 처음 코드를 짰을 때
# x, y = q.popleft()
# 위 이중 반복문에서 x, y를 사용하나 어차피 순회하면서 새로이 덮어씌워지기 때문에 상관 없다고 생각
# y는 내 생각대로 덮어써서 잘 순회되었지만 x가 업데이트 되지 않아 오류 발생
# 이중 반복문의 경우 하위 반복문이 한 바퀴 다 돌 때까지 상위 반복문이 업데이트 되지 않기 때문에 popleft()된 값에서 새로이 덮어씌워지지 않음
# 2차원 배열을 순회하는데 문제 발생
from collections import deque

def solution(maps):
    answer = []
    q = deque()
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 2차원 배열 순회
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            # 만약 방문 가능한 곳인데 방문한 적이 없다면, 큐에 삽입 & 방문 기록
            if maps[x][y] != "X" and visited[x][y] == 0:
                q.append((x, y))
                # 합계를 구하기 위해 list에 값 저장
                num_list = [int(maps[x][y])]
                visited[x][y] = 1
                # 연결된 곳 모두 방문
                while q:
                    # 여기서 문제 발생
                    _x, y = q.popleft()
                    
                    for i in range(4):
                        nx = _x + dx[i]
                        ny = y + dy[i]
                        # 범위 체크 & 방문 가능 & 첫 방문
                        if nx >= 0 and ny >= 0 and nx < len(maps) and ny < len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != "X":
                            res = int(maps[nx][ny])
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            # 값을 list에 저장
                            num_list.append(res)
                # 연결된 곳을 모두 방문하고 list에 있는 합계 계산
                answer.append(sum(num_list))
    
    # answer가 비어있다는 것 == 방문할 수 있는 곳이 없다는 것
    if not answer:
        return [-1]
    
    # answer 정렬 후 return
    return sorted(answer)