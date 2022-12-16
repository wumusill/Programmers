def solution(record):
    answer = []
    user_d = {}
    action_list = []

    for command in record:
        l = command.split()
        # Enter, Change라면
        if len(l) == 3:
            action, uid, nickname = l[0], l[1], l[2]

            # nickname 기록
            user_d[uid] = nickname

            # Enter는 행동과 id 기록, Change는 출력하지 않으므로 무시
            if action == 'Enter':
                action_list.append((action, uid))

        # Leave 라면 행동과 id 기록
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

#########################################################################

def solution(record):
    answer = []
    user = {}
    
    for log in record:
        logSplit = log.split(' ')
        if logSplit[0] == 'Enter':
            user[logSplit[1]] = logSplit[2]
            answer.append([logSplit[1], '님이 들어왔습니다.'])
        elif logSplit[0] == 'Leave':
            answer.append([logSplit[1], '님이 나갔습니다.'])
        elif logSplit[0] == 'Change':
            user[logSplit[1]] = logSplit[2]
    
    answer = [user[i[0]] + i[1] for i in answer]
        
    
    return answer


testcase = ['Enter uid1234 Muzi', 
            'Enter uid4567 Prodo',
            'Leave uid1234',
            'Enter uid1234 Prodo',
            'Change uid4567 Ryan']

print(solution(testcase))