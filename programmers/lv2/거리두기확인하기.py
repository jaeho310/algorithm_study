from collections import deque

def bfs(place, visited, start):
    queue = deque()
    queue.append(start)
    location = 1
    while queue:
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if place[nx][ny] != 'X':
                    location += 1
                    visited[nx][ny] = location


def check(place):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                visited[i][j] = 1
                bfs(place, visited, (i, j))
    for el in visited:
        print(el)


def solution(places):
    ans = []
    check(places[0])
    # for place in places:
    #     if check(place):
    #         ans.append(1)
    #     else:
    #         ans.append(0)
    # return True
if __name__ == '__main__':
    # P는 사람
    # O는 빈자리
    # X는 파티션
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
    ]
    print(solution(places))