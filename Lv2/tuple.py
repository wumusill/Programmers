def solution(s):
    answer = []
    # input 파싱
    s = s[2:len(s) - 2]
    s = list(s.split('},{'))

    # list로 type 변환
    for i in range(len(s)):
        s[i] = s[i].split(',')

    # 요소 길이 순으로 정렬
    s.sort(key=lambda x: len(x))

    for i in range(len(s)):
        for element in s[i]:
            if not answer:
                answer.append(int(element))
            if int(element) not in answer:
                answer.append(int(element))

    return answer