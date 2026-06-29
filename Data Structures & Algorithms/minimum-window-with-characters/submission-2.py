class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, table = {}, {}
        matches = 0
        bestl, bestr = None, None
        
        for c in t:
            table[c] = table.get(c, 0) + 1
            window[c] = 0
        
        l = 0
        while l < len(s) and s[l] not in table:
            l += 1
        
        r = l
        while r < len(s):
            if s[r] in table:
                window[s[r]] += 1
                if window[s[r]] == table[s[r]]:
                    matches += 1
            while matches == len(table):
                if not bestl or bestr - bestl > r - l:
                    bestl = l
                    bestr = r
                if s[l] in table:
                    window[s[l]] -= 1
                    if window[s[l]] < table[s[l]]:
                        matches -= 1
                l += 1
            r += 1
        if bestl == None:
            return ''
        return s[bestl: bestr + 1]

            