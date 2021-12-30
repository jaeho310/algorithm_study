location_dic = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
}


def is_last(first_x, first_y, ex_x, ex_y):
    if abs(first_x-ex_x) * abs(first_y-ex_y) == 2:
        return True
    return False

def solution1():
    alpha_location = ['A', 'B', 'C', 'D', 'E', 'F']
    location_list = []
    for i in range(1, 7):
        for j in alpha_location:
            location_list.append(j + str(i))
    ex_x = 0
    ex_y = 0
    first_x = 0
    first_y = 0
    isvalid = True
    order = ''
    for i in range(36):
        order = input()
        if order not in location_list:
            print('Invalid')
            return
        location_list.remove(order)
        x, y = location_dic[order[0]], int(order[1])
        if ex_x == 0:
            ex_x = x
            ex_y = y
            first_x = x
            first_y = y
        else:
            if abs(ex_x - x) * abs(ex_y - y) == 2:
                ex_x = x
                ex_y = y
            else:
                isvalid = False
                break
    if isvalid and is_last(first_x, first_y, ex_x, ex_y):
        print('Valid')
    else:
        print('Invalid')

if __name__ == '__main__':
    solution1()

