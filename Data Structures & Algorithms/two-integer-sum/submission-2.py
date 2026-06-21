class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in mem:
                return [mem[temp], i]
            mem[nums[i]] = i
        return []
