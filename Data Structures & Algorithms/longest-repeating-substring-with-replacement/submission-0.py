class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {s[0]: 1}
        l, r = 0, 1
        most = 1
        res = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            most = max(count.values()) 
            while r - l - most + 1 > k:
                count[s[l]] -= 1
                l += 1
                most = max(count.values())            
            r += 1
            res = max(res, r - l)

        return res