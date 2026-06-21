class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = height[l],  height[r]
        res = 0
        while l < r:
            if maxl <= maxr:
                l += 1
                res += max(0, maxl - height[l])
                maxl = max(maxl, height[l])
            else:
                r -= 1
                res += max(0, maxr - height[r])
                maxr = max(maxr, height[r])
        return res
