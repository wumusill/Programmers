def solution(phone_number):
    l = list(phone_number)
    for i in range(len(phone_number) - 4):
        l[i] = "*"
    return "".join(l)

def hide_number(s):
    return "*" * (len(s)-4) + s[-4:]

print(solution("01011112222"))
print(hide_number("027778888"))
