import sys


class Solution:
    def dfs(self, x, y, m, n, visited, word, idx, board, check):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited.append((x, y))
        if idx == len(word)-1:
            return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > m or ny < 0 or ny > n:
                continue
            if (nx, ny) not in visited:
                if word[idx] == board[nx][ny] and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    return self.dfs(nx, ny, m, n, visited, word, idx+1, board, check)
        return False

    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        check = [[0] for _ in range(m)]*n
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    res = self.dfs(i, j, m, n, [], word, 1, board, check)
                    if res:
                        print('true')
                        sys.exit(0)
        print('false')


if __name__ == '__main__':
    solution = Solution()
    solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
