import sys
from collections import deque

class Solution:
    word = ''
    board = None
    m = 0
    n = 0

    def dfs(self, x, y, check, idx):
        print(x, y)
        if idx == len(self.word):
            return True
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        current_x, current_y = x, y
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if nx < 0 or nx > self.m-1 or ny < 0 or ny > self.n-1:
                continue
            if self.word[idx] == self.board[nx][ny]:
                # check는 참조타입이라 재귀호출시해서 변경되면 다시 복구가 안된다.
                if check[nx][ny] != 1:
                    check[nx][ny] = 1
                    res = self.dfs(nx, ny, check, idx+1)
                    if res:
                        return True
        return False

    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        self.m = m
        self.n = n
        self.word = word
        self.board = board
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    check = []
                    for _ in range(m):
                        check.append([0 for i in range(n)])
                    check[i][j] = 1
                    res = self.dfs(i, j, check, 1)
                    if res:
                        return True
        return False


if __name__ == '__main__':
    solution = Solution()
    boards = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    words = "ABCESEEEFS"
    print(words)
    print(solution.exist(boards, words))



# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCCED"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "SEE"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCB"