import sys
from collections import deque

class Solution:
    word = ''
    board = None
    m = 0
    n = 0

    def dfs(self, x, y, visited, idx):
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
            if self.word[idx] == self.board[nx][ny] and (nx,ny) not in visited:
                visited.append((nx, ny))
                res = self.dfs(nx, ny, visited, idx + 1)
                if res:
                    return True
                else:
                    visited.pop()
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
                    visited = []
                    visited.append((i,j))
                    res = self.dfs(i, j, visited, 1)
                    if res:
                        return True
        return False


if __name__ == '__main__':
    solution = Solution()
    boards = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    words = "ABCESEEEFS"
    print(words)
    print(solution.exist(boards, words))



# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCCED"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "SEE"
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# "ABCB"

# 실패
# [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
# "A B C E S E E E F S"
# A B C E
# S F E S
# A D E E
# True가 나와야함
