class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem = defaultdict(int) #keys: nums, values: count
        res = []
        for num in nums:
            mem[num] += 1
        arr = list(sorted(mem.items(), key = lambda item: item[1]))
        while len(res) < k:
            res.append(arr.pop()[0])
        return res