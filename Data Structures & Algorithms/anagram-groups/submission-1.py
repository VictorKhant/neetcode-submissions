class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            temp = ''.join(sorted(s))
            if temp in seen:
                seen[temp].append(s)
            else:
                seen[temp] = [s]
        return list(seen.values())