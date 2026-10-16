class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        res = []
        for ind, point in enumerate(points):
            print(point[0], point[1])
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            print(dist,ind)
            distances.append((dist, ind))
            print(distances)

        heapq.heapify(distances)
        # i=0
        # while i < k:
        #     temp = heapq.heappop(distances)
        #     res.append(points[temp[1]])
        #     i+=1
        #     if i == k:
        #         break
        for i in range(k):
            temp = heapq.heappop(distances)
            res.append(points[temp[1]])
        return res
        