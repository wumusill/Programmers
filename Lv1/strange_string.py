def solution(s):
    l = list(s.split(" "))
    new_l = []
    for word in l:
        spells = list(word)
        for i in range(0, len(spells), 2):
            spells[i] = spells[i].upper()
        new_l.append(''.join(spells))
    return ' '.join(new_l)


s = 'try hello world'
print(solution(s))