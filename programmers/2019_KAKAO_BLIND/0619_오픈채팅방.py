def solution(record):
    ans = []; user_list = {}
    for x in record:
        if x.split(' ')[0] == 'Enter' or x.split(' ')[0] == 'Change':
            user_list[x.split(' ')[1]] = x.split(' ')[2]
    for x in record:
        if x.split(' ')[0] == 'Enter':
            ans.append(user_list[x.split(' ')[1]] + '님이 들어왔습니다.')
        elif x.split(' ')[0] == 'Leave':
            ans.append(user_list[x.split(' ')[1]] + '님이 나갔습니다.')
    return ans

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
