def solution(s, n):
    l = list(s)
    for i in range(len(l)):
        if l[i].islower():
            if l[i] == 'z':
                l[i] = chr(ord(l[i]) - 25 + (n-1))
            else:
                ascii_of_new = ord(l[i]) + n
                if ascii_of_new <= 122:
                    l[i] = chr(ascii_of_new)
                else:
                    l[i] = chr(ascii_of_new - 26)
        elif l[i].isupper():
            if l[i] == 'Z':
                l[i] = chr(ord(l[i]) - 25 + (n-1))
            else:
                ascii_of_new = ord(l[i]) + n
                if ascii_of_new <= 90:
                    l[i] = chr(ascii_of_new)
                else:
                    l[i] = chr(ascii_of_new - 26)
    return ''.join(l)


def solution_2(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
    return "".join(s)

print(solution("a B z", 4))
print(solution_2("a B z", 4))