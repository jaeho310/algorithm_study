from collections import defaultdict

if __name__ == '__main__':
    n = input()
    num_dict = defaultdict(float)
    for i in n:
        num = int(i)
        if num == 9 or num == 6:
            num_dict[6] += 0.5
            continue
        num_dict[num] += 1
    items = list(num_dict.items())
    items = sorted(items, key=lambda x: x[1], reverse=True)
    answer = items[0][1]
    if answer - int(answer) != 0:
        print(int(answer+0.5))
    else:
        print(int(answer))
