class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(numbers)):
            if target - numbers[i] in mem:
                return [mem[target - numbers[i]], i + 1]
            mem[numbers[i]] = i + 1
        return None