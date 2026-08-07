class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d_points = []
        def distance(x1, y1, x2, y2):
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        for x, y in points:
            d = -distance(0, 0, x, y)
            heapq.heappush(d_points, [d,x, y])
            if len(d_points) > k:
                heapq.heappop(d_points)
            
        res = []
        while d_points:
            _, x, y = heapq.heappop(d_points)
            res.append([x, y])
        return res
        