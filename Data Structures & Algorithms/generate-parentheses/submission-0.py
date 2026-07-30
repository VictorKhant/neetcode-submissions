class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(s, opens, closes):
            if len(s) == 2 * n:
                result.append(s)
                return
            if opens < n:
                backtrack(s + '(', opens + 1, closes)
            if closes < opens:
                backtrack(s + ')', opens, closes + 1)
            
        backtrack('',0, 0)
        return result