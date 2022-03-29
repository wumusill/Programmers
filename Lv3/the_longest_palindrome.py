# 다음 글자가 같은지 체크한다.
    # 같다면 두 글자를 하나로 보고 앞뒤로 같은지 확인해간다.
    # 같더라도 아래 다른 경우도 확인해서 더 큰 값을 리턴한다.

# 다르다면 앞뒤로 같은지 확인해간다.

def solution(s):
    answer = 1
    for i in range(1, len(s) - 1):
        if s[i] == s[i + 1]:
            for j in range(1, 3):
                front_idx = 1
                palindrome = j
                back_idx = j

                while i - front_idx >= 0 and i + back_idx < len(s):
                    if s[i - front_idx] == s[i + back_idx]:
                        palindrome += 2
                        front_idx += 1
                        back_idx += 1
                    else:
                        break
                    answer = max(answer, palindrome)

        else:
            palindrome = 1
            front_idx = 1
            back_idx = 1

        while i - front_idx >= 0 and i + back_idx < len(s):
            if s[i - front_idx] == s[i + back_idx]:
                palindrome += 2
                front_idx += 1
                back_idx += 1
            else:
                break
            answer = max(answer, palindrome)
    return answer


print(solution('abacde'))  # 3
print(solution('abcdcba'))  # 7
print(solution('aaaaaa'))  # 6
print(solution('abcabcdcbae'))  # 7
print(solution("aaaa"))  # 4
print(solution("abcde"))  # 1
print(solution("a"))  # 1
print(solution('abcaqwertrewqq'))  # 9
print(solution("abcbaqwqabcba"))  # 13
print(solution('abba'))  # 4
print(solution('abaabaaaaaaa'))  # 7
print(solution('rnwkaaaaa'))  # 5
