class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        result = []
        for each in nums:
            if each in dic:
                dic[each] += 1
            else:
                dic[each] = 1
        sortedList = sorted(dic.items(), key = lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(sortedList[i][0])
        return result