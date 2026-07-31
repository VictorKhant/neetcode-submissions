class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = []
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j] and (l <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
        
        def backtrack(start, curr):
            if start >= n:
                res.append(curr.copy())
            for end in range(start, n):
                if dp[start][end]:
                    curr.append(s[start: end + 1])
                    backtrack(end + 1, curr)
                    curr.pop()
        backtrack(0,[])
        return res
