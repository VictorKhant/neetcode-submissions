class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if i >= len(candidates):
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                if total + candidates[j] > target:
                    return
                curr.append(candidates[j])
                backtrack(j + 1, curr, total + candidates[j])
                curr.pop()
        backtrack(0, [], 0)
        return res
