class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left<right:
            while left < right and not self.alphaNum(s[right]):
                right -= 1
            while left < right and not self.alphaNum(s[left]):
                left += 1
            if s[right].lower() != s[left].lower():
                return False
            left += 1
            right -= 1
        return True
    def alphaNum(self, n):
        return (ord('A') <= ord(n) <= ord('Z') or 
                ord('a') <= ord(n) <= ord('z') or 
                ord('0') <= ord(n) <= ord('9'))