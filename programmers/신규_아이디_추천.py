def case_1(s):
    return s.lower()

def case_2(s):
    answer = ''
    for c in s:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    return answer

def case_3(s):
    while True:
        temp = len(s)
        s = s.replace("..", ".")
        if temp == len(s):
            break
    return s


def case_4(s):
    if s[0] == ".":
        s = s[1:]
    elif s[-1] == ".":
        s = s[:-1]
    return s


def case_5(s):
    if len(s) == 0:
        s = "a"
    return s


def case_6(s):
    if len(s) >= 16:
        s = s[:15]
    if s[-1] == ".":
        s = s[:-1]
    return s


def case_7(s):
    if len(s) <= 2:
        return case_7(s + s[-1])
    return s
def solution(new_id):
    # 1단계
    new_id = case_1(new_id)

    # 2단계
    new_id = case_2(new_id)

    # 3단계
    new_id = case_3(new_id)

    # 4단계
    new_id = case_4(new_id)

    # 5단계
    new_id = case_5(new_id)

    # 6단계
    new_id = case_6(new_id)

    # 7단계
    new_id = case_7(new_id)

    return new_id

# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
if __name__ == '__main__':
    print(solution("abcdefghijklmn.p"))
    pass