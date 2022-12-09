# 무지성 구현 + 조금의 정규방정식
import re


def solution(new_id):
    # 1단계 : 대문자를 모두 소문자로
    step_1 = new_id.lower()

    # 2단계 "-", "_", ".", 알파벳, 숫자 제외하고 모두 제거
    # "-"의 경우 정규표현식에서 의미를 갖고 있는 문자라서 앞에 "\" 추가
    step_2 = re.sub("[^_\-.a-z0-9]", "", step_1)

    # 3단계
    # 임의의 리스트, 맨 앞글자 추가
    l = []
    l += step_2[0]

    # 두 번째 글자부터 순회하면서 앞글자가 "." 이라면 continue
    # "."이 아니라면 리스트에 추가
    for j in range(1, len(step_2)):
        if step_2[j] == '.' and l[-1] == '.':
            continue
        l.append(step_2[j])

    # # 3단계 with re
    # # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    # new_id = re.sub(r"[\.]+", ".", step_2)
    # l = list(new_id)

    # 4단계 : 리스트는 현재 글자들이 원소로 있음
    # 맨 앞이 "." 이라면 슬라이싱으로 제거
    if l[0] == '.':
        l = l[1:]

    # 마지막 글자가 "." 이라면 마찬가지 슬라이싱으로 제거
    if len(l) != 0 and l[-1] == '.':
        l = l[:len(l) - 1]

    # 5단계 : 빈 문자열이라면(=리스트가 비어있다면?) "a" 추가
    if len(l) == 0:
        l.append('a')

    # 6단계 : 길이가 16자 이상이라면 첫 15개를 제외한 나머지 문자 제거
    if len(l) >= 16:
        l = l[:15]

    # 제거 후 마지막 글자가 "." 이라면 그것도 제거
    if l[-1] == '.':
        l = l[:len(l) - 1]

    # 7단계 : 글자의 길이가 2 이하라면 3이 될 때까지 마지막 문자를 추가
    while len(l) <= 2:
        l.append(l[-1])

    # 리스트 원소들을 결합하며 단어로 반환
    return "".join(l)