from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, sub):
            if not curr:
                res.append(sub.copy())
                return
            for i in range(len(curr)):
                item = curr.popleft()
                sub.append(item)
                dfs(curr, sub)
                sub.pop()
                curr.append(item)
        dfs(deque(nums), [])
        return res
            