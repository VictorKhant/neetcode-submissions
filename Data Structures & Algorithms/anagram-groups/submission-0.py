class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        result = []
        for each in strs:
            temp = ''.join(sorted(each))
            if temp in dic:
                dic[temp] += [each]
            else:
                dic[temp] = [each]
        for i in dic.values():
            result.append(i)
        return result