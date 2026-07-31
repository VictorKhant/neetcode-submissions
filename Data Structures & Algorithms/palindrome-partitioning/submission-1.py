class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, curr):
            if start >= len(s):
                res.append(curr.copy())
                return
            for end in range(start, len(s)):
                substring = s[start:end + 1]
                if isPalindrome(substring):
                    curr.append(substring)
                    backtrack(end + 1, curr)
                    curr.pop()
        
            
        def isPalindrome(s):
            left, right = 0, len(s) - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True
        backtrack(0, [])
        return res
