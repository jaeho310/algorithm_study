def solution(record):
    # 밖에서 닉네임을 변경하면 로그에 남지 않는다.
    name_dict = dict()
    res = []
    for el in record:
        split = el.split()
        action = split[0]
        if action == "Change":
            name_dict[split[1]] = split[2]
        elif action == "Enter":
            if split[1] not in name_dict.keys():
                name_dict[split[1]] = split[2]
            else:
                name_dict[split[1]] = split[2]
    print(name_dict)
    for el in record:
        split = el.split()
        action = split[0]
        if action == "Enter":
            uid = split[1]
            name = split[2]
            if uid in name_dict.keys():
                name = name_dict[uid]
            res.append(name+"님이 들어왔습니다.")
        elif action == "Leave":
            res.append(name_dict[split[1]]+"님이 나갔습니다.")
    return res

if __name__ == '__main__':
    l = solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"])
    print('\n'.join(l))