class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        dia1 = set()
        dia2 = set()
        prevCol = set()
        def backtrack(count):
            if count == n:
                res.append(["".join(row) for row in board])
            for i in range(n):
                if i in prevCol or (count - i) in dia1 or (count + i) in dia2:
                    continue
                board[count][i] = 'Q'
                prevCol.add(i)
                dia1.add(count - i)
                dia2.add(count + i)
                backtrack(count + 1)
                prevCol.remove(i)
                dia1.remove(count - i)
                dia2.remove(count + i)
                board[count][i] = '.'
        backtrack(0)
        return res
