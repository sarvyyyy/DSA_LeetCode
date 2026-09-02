class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]
        def is_valid(row, col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True
                
        def backTrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_valid(row,col):
                    board[row][col] = "Q"
                    backTrack(row+1)
                    board[row][col] = "."

        backTrack(0)
        return res