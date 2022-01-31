change_list = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]

def solution(s):
    for el in change_list:
        s = s.replace(el, str(change_list.index(el)))
    return s

if __name__ == '__main__':
    s = 'one4seveneight'
    print(int(solution(s)))