def solution(record):
    answer = []
    user_d = {}
    action_list = []

    for command in record:
        l = command.split()
        if len(l) == 3:
            action, uid, nickname = l[0], l[1], l[2]
            user_d[uid] = nickname

            if action == 'Enter':
                action_list.append((action, uid))

        else:
            action, uid = l[0], l[1]
            action_list.append((action, uid))

    for action, uid in action_list:
        if action == 'Enter':
            answer.append(user_d[uid]+'님이 들어왔습니다.')
        else:
            answer.append(user_d[uid]+'님이 나갔습니다.')

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))