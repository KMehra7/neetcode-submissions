class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        res = []
        for ind, point in enumerate(points):
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            distances.append((dist, ind))
        
        heapq.heapify(distances)
        for i in range(k):
            temp = heapq.heappop(distances)
            res.append(points[temp[1]])
        return res
        