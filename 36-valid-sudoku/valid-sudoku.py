class Solution:
    def isValidSudoku(self, board: List[List[str]]):
        
        for i in range(len(board)):
            row=[]
            col=[]
            for j in range(len(board)):
                if board[i][j]!= '.':
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])
            
                if board[j][i]!= '.':
                    if board[j][i] in col:
                        return False
                    col.append(board[j][i])

        c1=0
        c2=0
        while c1<9:
            box=[]
            for i in range(3):
                for j in range(3):
                    if board[c1+i][c2+j]!='.':
                        if board[c1+i][c2+j] in box:
                            return False
                        box.append(board[c1+i][c2+j])
                        
            c2+=3
            if c2==9:
                c2=0
                c1+=3
        return True

