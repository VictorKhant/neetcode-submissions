class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_max = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                h = min(heights[i], heights[j])
                w = j - i
                if h * w > current_max:
                    current_max = h * w
        return current_max