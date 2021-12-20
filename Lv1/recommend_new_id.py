def solution(new_id):
    step_1 = new_id.lower()

    not_in = "~!@#$%^&*()=+[{]}:?,<>/"
    step_2 = ''.join(x for x in step_1 if x not in not_in)

    l = []
    l += step_2[0]

    for j in range(1, len(step_2)):
        if step_2[j] == '.' and l[-1] == '.':
            continue
        l.append(step_2[j])

    if l[0] == '.':
        l = l[1:]

    if len(l) != 0 and l[-1] == '.':
        l = l[:len(l) - 1]

    if len(l) == 0:
        l.append('a')

    if len(l) >= 16:
        l = l[:15]

    if l[-1] == '.':
        l = l[:len(l) - 1]

    while len(l) <= 2:
        l.append(l[-1])
    return "".join(l)