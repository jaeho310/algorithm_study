from collections import defaultdict

if __name__ == '__main__':
    data = defaultdict(int)
    target = tuple(map(int, input().split()))
    i = 1
    while True:
        earth = i % 15
        sun = i % 28
        moon = i % 19
        if earth == 0: earth = 15
        if sun == 0: sun = 28
        if moon == 0: moon = 19
        data[earth, sun, moon] = i
        if target in data:
            print(data[target])
            break
        i += 1
