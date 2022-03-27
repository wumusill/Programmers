def solution(id_list, report, k):
    answer = []
    suspended = []
    reporting_dict = {user_name : list() for user_name in id_list}
    reported_dict = {user_name: 0 for user_name in id_list}

    for content in report:
        reporting, reported = content.split()
        if reported not in reporting_dict[reporting]:
            reporting_dict[reporting].append(reported)
            reported_dict[reported] += 1

    for user_name in id_list:
        if reported_dict[user_name] >= k:
            suspended.append(user_name)

    for user_name in id_list:
        mail = 0
        if user_name not in reporting_dict.keys():
            answer.append(mail)
        else:
            for reported_user in reporting_dict[user_name]:
                if reported_user in suspended:
                    mail += 1
            answer.append(mail)
    return answer


print(solution(['muzi', 'frodo', 'apeach', 'neo'], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(['con', 'ryan'], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

###############################################################################

def solution_2(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer