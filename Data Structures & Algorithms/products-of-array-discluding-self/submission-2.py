class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        product[0] = nums[0]
        reverse = [1] * len(nums)
        reverse[-1] = nums[-1]
        result = [1] * len(nums)
        for i in range(1, len(nums) - 1):
            product[i] = product[i - 1] * nums[i]
        for i in range(len(nums) - 2, 0, -1):
            reverse[i] = reverse[i + 1] * nums[i]
        result[0] = reverse[1]
        result[-1] = product[-2]
        for i in range(1, len(nums) - 1):
            before = product[i - 1] if i - 1 >= 0 else 0
            after = reverse[i + 1] if i + 1 < len(nums) else 0
            result[i] = before * after
    
        return result

