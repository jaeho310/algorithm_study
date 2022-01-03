def value_multi(m, n):
    temp = dict()
    for k, v, in m.items():
        temp[k] = v * n
    return temp

def value_adder(m1, m2):
    temp = {'C': 0, 'H': 0, 'O': 0}
    temp['C'] = m1['C'] + m2['C']
    temp['H'] = m1['H'] + m2['H']
    temp['O'] = m1['O'] + m2['O']
    return temp


def solution(m1, m2, m3):
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                res1 = value_adder(value_multi(m1, i), value_multi(m2, j))
                res2 = value_multi(m3, k)
                if res1 == res2:
                    return i, j, k



if __name__ == '__main__':
    order = input()
    m1 = {'C': 0, 'H': 0, 'O': 0}
    m2 = {'C': 0, 'H': 0, 'O': 0}
    m3 = {'C': 0, 'H': 0, 'O': 0}
    m_list = []
    m_list.append(m1)
    m_list.append(m2)
    m_list.append(m3)
    m_idx = 0
    for i in range(len(order)):
        if order[i] == '+' or order[i] == '=':
            m_idx += 1
        if order[i] == 'C' or order[i] == 'H' or order[i] == 'O':
            if i+1 >= len(order):
                m_list[m_idx][order[i]] += 1
                break
            if order[i+1].isdigit():
                m_list[m_idx][order[i]] += int(order[i+1])
            else:
                m_list[m_idx][order[i]] += 1
    ans = solution(m_list[0], m_list[1], m_list[2])
    for a in ans:
        print(str(a), end=' ')

