class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(0,9):
            seen = set()
            for i in range(0,9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        for col in range(0,9):
            seen = set()
            for i in range(0,9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                seen = set()
                for i in range(row,row+3):
                    for j in range(col, col+3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True

