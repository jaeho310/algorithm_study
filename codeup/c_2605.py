graph = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, color):
    global graph
    # for i in range(4):
    pass



if __name__ == '__main__':
    graph.append(list(map(int, input().split())))
    for i in range(7):
        for j in range(i, 7):
            dfs(i, j, graph[i][j])

