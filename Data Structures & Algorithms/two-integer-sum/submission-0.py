class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            current = nums[i]
            result = [i]
            for j in range(i+1, len(nums)):
                if current + nums[j] == target:
                    result.append(j)
                    return result
        return 

            


        