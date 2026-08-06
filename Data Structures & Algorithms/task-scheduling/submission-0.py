class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort(reverse=True)
        idle = (count[0] - 1) * n

        for item in count[1:]:
            idle -= min(count[0] - 1, item)
        return max(0, idle) + len(tasks)
