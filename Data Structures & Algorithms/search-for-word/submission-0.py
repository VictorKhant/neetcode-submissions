class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def backtrack(r, c, w):
            if len(w) == 0:
                return True
            if  r >= rows or c >= cols or r < 0 or c < 0 or board[r][c] != w[0]:
                return False
            board[r][c] = '#'
            l = backtrack(r, c - 1, w[1:])
            ri = backtrack(r, c + 1, w[1:])
            u = backtrack(r - 1, c, w[1:])
            d = backtrack(r + 1, c, w[1:]) 
            board[r][c] = w[0]
            return l or ri or u or d
        
        return any(backtrack(r, c, word) for r in range(rows) for c in range(cols))