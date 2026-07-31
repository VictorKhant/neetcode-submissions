from collections import deque
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(curr, sub):
            if not curr:
                res.append(sub.copy())
                return
            for _ in range(len(curr)):
                item = curr.popleft()
                sub.append(item)
                backtrack(curr, sub)
                curr.append(item)
                sub.pop()

        backtrack(deque(nums), [])
        return res