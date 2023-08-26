def solution(msg):
    answer = []
    # 사전 정의
    d = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, 
         "J":10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17,
         "R":18, "S":19, "T":20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}
    a, b = 0, 1
    cnt = 27
    while a < len(msg):
        # 단어 슬라이싱 순회
        for i in range(b, len(msg) + 1):
            # 사전에 있으면 continue, 그러나 더 이상 탐색할 글자가 없다면 정답에 코드 추가해야 함
            # 마지막이라면, 더 이상 탐색할 글자가 없다면 코드 추가하고 while 문이 돌지 않도록 index 갱신
            if msg[a:i] in d.keys():
                if i == len(msg):
                    answer.append(d[msg[a:i]])
                    a = len(msg)
                    break
                else:
                    continue
            # 사전에 존재하지 않는 단어면, 사전에 추가 후 그 전 단어까지 정답에 코드 추가 후 그 다음 글자부터 탐색할 수 있게 index 갱신
            elif msg[a:i] not in d.keys():
                d[msg[a:i]] = cnt
                cnt += 1
                answer.append(d[msg[a:i-1]])
                a = i - 1
                b = i
                break
        
    return answer
##########################################################################################
# 더 이해하기 쉬운 비슷한 로직의 다른 코드
def solution(msg):
    # 사전 정의
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        # 단어가 사전에 있다면 코드 정답에 추가
        if msg in d:
            answer.append(d[msg])
            break
        # 문자열 앞에서부터 슬라이싱 탐색
        for i in range(1, len(msg)+1):
            # 사전에 없는 단어가 등장하면
            # 사전에 있는 글자까지 코드 정답에 추가
            # 사전에 처음 등장한 단어 추가
            # 정답에 추가된 글자 제거 -> 그 다음 글자부터 반복 수행
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer