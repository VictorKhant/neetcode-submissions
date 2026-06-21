class Solution:
    def trap(self, height: List[int]) -> int:
       res = 0
       l, r = 0, len(height) - 1
       maxl, maxr = height[l], height[r]
       while l < r:
        if maxl < maxr:
            l += 1
            res += max(maxl - height[l], 0)
            maxl = max(maxl, height[l])
        else:
            r -= 1
            res += max(maxr - height[r], 0)
            maxr = max(maxr, height[r])
       return res