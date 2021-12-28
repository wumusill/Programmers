def solution(s):
    if len(s) == 4 or len(s) == 6:
        S = s.upper()
        if s == S:
            return True
    return False

# s.isdigit() : 문자열 구성이 모두 숫자인지 확인하는 메소
def solution_2(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)

def solution_3(s):
    return s.isdigit() and len(s) in (4, 6)

def solution_4(s):
    try:
        int(s)
    except:
        return False
    return  len(s) == 4 or len(s) == 6
