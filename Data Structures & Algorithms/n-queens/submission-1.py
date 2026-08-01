class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        res = []
        dia1 = set()
        dia2 = set()
        def backtrack(count, prevCol):
            if count == n:
                res.append(["".join(row) for row in board])
            for i in range(n):
                if i in prevCol or (count - i) in dia1 or (count + i) in dia2:
                    continue
                board[count][i] = 'Q'
                prevCol.add(i)
                dia1.add(count - i)
                dia2.add(count + i)
                backtrack(count + 1, prevCol)
                prevCol.remove(i)
                dia1.remove(count - i)
                dia2.remove(count + i)
                board[count][i] = '.'

        # def isValid(r, c):
        #     tempR, tempC = r, c
        #     while r - 1 >= 0 and c - 1 >= 0:
        #         r -= 1
        #         c -= 1
        #         if board[r][c] == 'Q':
        #             return False

        #     r, c = tempR, tempC
        #     #row + 1, col + 1
        #     while r + 1 < n and c + 1<  n:
        #         r += 1
        #         c += 1
        #         if board[r][c] == 'Q':
        #             return False

        #     r, c = tempR, tempC
        #     while r + 1 < n and c - 1 >= 0:
        #         r += 1
        #         c -= 1
        #         if board[r][c] == 'Q':
        #             return False

        #     r, c = tempR, tempC
        #     while r - 1 >= 0 and c + 1 < n:
        #         r -= 1
        #         c += 1
        #         if board[r][c] == 'Q':
        #             return False
        #     return True
        backtrack(0, set())
        return res
