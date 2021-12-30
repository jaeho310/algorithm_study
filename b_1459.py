if __name__ == '__main__':
    x, y, time_normal, time_diagonal = map(int, input().split())
    # 대각선으로 갈 필요 x
    if time_normal * 2 <= time_diagonal or x == 0 or y == 0:
        print(time_normal * (x + y))
    else:
        diagonal_cnt = 0
        while x != 0 and y != 0:
            x -= 1
            y -= 1
            diagonal_cnt += 1
        print(time_diagonal * diagonal_cnt + time_normal * (x + y))
1