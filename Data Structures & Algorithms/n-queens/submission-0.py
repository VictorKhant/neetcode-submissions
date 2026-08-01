class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        def backtrack(count, prevCol):
            if prevCol and not isValid(count - 1, prevCol[-1]):
                return
            if count == n:
                res.append(["".join(row) for row in board])
            for i in range(n):
                if i in prevCol:
                    continue
                board[count][i] = 'Q'
                prevCol.append(i)
                backtrack(count + 1, prevCol)
                prevCol.pop()
                board[count][i] = '.'

        def isValid(r, c):
            tempR, tempC = r, c
            #row - 1, col - 1
            while r - 1 >= 0 and c - 1 >= 0:
                r -= 1
                c -= 1
                if board[r][c] == 'Q':
                    return False

            r, c = tempR, tempC
            #row + 1, col + 1
            while r + 1 < n and c + 1<  n:
                r += 1
                c += 1
                if board[r][c] == 'Q':
                    return False

            r, c = tempR, tempC
            #row + 1, col - 1
            while r + 1 < n and c - 1 >= 0:
                r += 1
                c -= 1
                if board[r][c] == 'Q':
                    return False

            r, c = tempR, tempC
            #row - 1, col + 1
            while r - 1 >= 0 and c + 1 < n:
                r -= 1
                c += 1
                if board[r][c] == 'Q':
                    return False
            return True
        backtrack(0, [])
        return res
