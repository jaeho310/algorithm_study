if __name__ == '__main__':
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    # 문제의 핵심은 끝나는 시간이 빠른걸로 먼저 sort, 그후 시작하는 시간이 빠른걸로 sort
    # 이 정렬이 구현되면 그리디 알고리즘을 사용할 수 있다
    rooms = sorted(rooms, key=lambda x: (x[1], x[0]))
    ans = 1
    # [0][1]은 가장 빨리끝나고 가장 빨리 시작하는 회의실 예약
    end_time = rooms[0][1]
    for i in range(1, n):
        # 다음 시작시간이 끝나는 시간보다 크면 선택하면 되고, 이미 sort되있으므로 시작시간이 같은건 신경쓰지 않아도 된다.
        if rooms[i][0] >= end_time:
            ans += 1
            end_time = rooms[i][1]
    print(ans)




