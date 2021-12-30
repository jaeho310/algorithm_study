def solution():
    n = int(input())
    if n == 1:
        return 0
    candidate = []
    for i in range(n):
        candidate.append(int(input()))
    answer = 0
    while True:
        wanted_max = candidate.pop(0)
        max_value = max(candidate)
        if wanted_max > max_value:
            break
        candidate[candidate.index(max_value)] -= 1
        candidate.insert(0, wanted_max+1)
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution())
