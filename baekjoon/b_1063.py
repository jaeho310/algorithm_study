chess = [[0] * 8] * 8
location_dict = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H'
}

checkList = [0,1,2,3,4,5,6,7]


def solution(order, a, b, c, d):
    king_x = a
    king_y = b
    stone_x = c
    stone_y = d
    for o in order:
        king_x_next = king_x
        king_y_next = king_y
        stone_x_next = stone_x
        stone_y_next = stone_y
        if o == 'R':
            king_y_next += 1
            stone_y_next += 1
        elif o == 'L':
            king_y_next -= 1
            stone_y_next -= 1
        elif o == 'T':
            king_x_next -= 1
            stone_x_next -= 1
        elif o == 'B':
            king_x_next += 1
            stone_x_next += 1
        elif o == 'RT':
            king_x_next -= 1
            king_y_next += 1
            stone_x_next -= 1
            stone_y_next += 1
        elif o == 'LT':
            king_x_next -= 1
            king_y_next -= 1
            stone_x_next -= 1
            stone_y_next -= 1
        elif o == 'RB':
            king_x_next += 1
            king_y_next += 1
            stone_x_next += 1
            stone_y_next += 1
        elif o == 'LB':
            king_x_next += 1
            king_y_next -= 1
            stone_x_next += 1
            stone_y_next -= 1

        # if king_x_next < 0 or king_x_next > 7 or king_y_next < 0 or king_y_next > 7 or stone_x_next < 0 or stone_x_next > 7 or stone_y_next < 0 or stone_y_next > 7:
        if king_x_next not in checkList:
            continue
        if king_y_next not in checkList:
            continue
        if king_x_next == stone_x and king_y_next == stone_y:
            if stone_x_next not in checkList:
                continue
            if stone_y_next not in checkList:
                continue
            stone_x = stone_x_next
            stone_y = stone_y_next
        king_x = king_x_next
        king_y = king_y_next

    return (king_x, king_y), (stone_x, stone_y)


if __name__ == '__main__':
    k, s, n = input().split(' ')
    a = 8 - int(k[1])
    b = location_dict[k[0]]
    c = 8 - int(s[1])
    d = location_dict[s[0]]
    # chess[a][b] = 1
    # chess[c][d] = 2
    order = []
    for _ in range(int(n)):
        order.append(input())
    king_position, stone_position = solution(order, a, b, c, d)
    print(king_position, stone_position)
    king_res = location_dict[king_position[1]] + str(8-king_position[0])
    stone_res = location_dict[stone_position[1]] + str(8-stone_position[0])
    # king_res = location_dict[8-king_position[1] + str(king_position[0])
    # stone_res = location_dict[stone_position[0]] + str(8-stone_position[1])
    print(king_res)
    print(stone_res)
