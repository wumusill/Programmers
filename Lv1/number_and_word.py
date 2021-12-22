dic = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }

def solution(s):
    string = ""
    answer = ""
    for i in list(s):
        string += i
        if i in dic.values():
            answer += i
            string = ""
        if string in dic.keys():
            answer += dic.get(string)
            string = ""
    return int(answer)

# def solution(s):
#     answer = s
#     for key, value in dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)