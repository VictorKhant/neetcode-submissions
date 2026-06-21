class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            if a > 0:
                break
            b, c = i + 1, len(nums) - 1
            while b < c:
                threeSum = nums[b] + nums[c] + a
                if threeSum > 0:
                    c -= 1
                elif threeSum < 0:
                    b += 1
                else:
                    res.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
        return res
            