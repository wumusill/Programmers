import re

def solution(str1, str2):
    # 소문자로 통일
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 중복 허용이므로 리스트로 선언
    set1 = []
    set2 = []
    
    # str1 2글자씩 조회
    for i in range(1, len(str1)):
        word = str1[i-1:i+1]
        # 만약 알파벳 아닌게 없다면
        if not bool(re.search("[^a-z]", word)):
            set1.append(word)

    # str2 2글자씩 조회    
    for i in range(1, len(str2)):
        word = str2[i-1:i+1]
        # 만약 알파벳 아닌게 없다면
        if not bool(re.search("[^a-z]", word)):
            set2.append(word)

    # 중복 허용 교집합
    inter = []

    # 중복 허용 합집합
    union = []
    
    # 합집합을 str1 로 정의하고
    # str2 단어를 순회하면서 str1 에 없다면 합집합에 추가
    # str1 에 있다면 제거
    a_tmp = set1.copy()
    union = set1.copy()
    for i in set2:
        if i not in a_tmp:
            union.append(i)
        else:
            a_tmp.remove(i)
    
    # str2 단어를 순회하면서 str1에 있는 단어라면
    # str1 에서 제거하고 교집합에 추가
    for i in set2:
        if i in set1:
            set1.remove(i)
            inter.append(i)
            
    if len(union) > 0:
        return int(len(inter) / len(union) * 65536)
    else:
        return 65536