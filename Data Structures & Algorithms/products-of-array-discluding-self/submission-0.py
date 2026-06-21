class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i in range(len(nums)):
            temp = nums[0:i] + nums[i+1:]
            for num in temp:
                result[i] = result[i]*num
        return result
